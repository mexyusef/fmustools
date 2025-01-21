import decimal, json, os, sys, time
import psycopg2
from configparser import ConfigParser

import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


ACCESS_KEY = ''
SECRET_KEY = ''

""" :type : pyboto3.rds """
RDS_DB_SUBNET_GROUP = "my-rds-db-subnet-group"
RDS_SECURITY_GROUP_NAME = "my-rds-public-sg"
RDS_DB_SUBNET_NAME = 'my-rds-subnet-group'

SQS_QUEUE_URL = ''


"""
[postgresql]
host=postgresqlinstanceidentifier.xxxxxxxxxx.eu-west-3.rds.amazonaws.com
database=PostgreSQLDBInstance
user=postgres
password=mypostgrespassword
"""
DB_CONFIG_FILE = os.path.dirname(__file__) + '/database.ini'


class ClientFactory:
    def __init__(self, client):
        self._client = boto3.client(client, region_name="eu-west-3")

    def get_client(self):
        return self._client


class DynamoDBClient(ClientFactory):
    def __init__(self):
        super().__init__('dynamodb')


class RDSClient(ClientFactory):
    def __init__(self):
        super().__init__('rds')


class EC2Client(ClientFactory):
    def __init__(self):
        super().__init__('ec2')


class DynamoDB:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.dynamodb """

    def create_table(self, table, attribute_definitions, key_schema, iops):
        print("Creating DynamoDB table...")
        return self._client.create_table(
            TableName=table,
            AttributeDefinitions=attribute_definitions,
            KeySchema=key_schema,
            ProvisionedThroughput=iops
        )

    def describe_table(self, table):
        print("Describing DynamoDB table with name " + table)
        return self._client.describe_table(TableName=table)

    def update_read_write_capacity(self, table_name, new_read_capacity, new_write_capacity):
        print("Updating Provisioned Throughput of table with name " + table_name)
        return self._client.update_table(
            TableName=table_name,
            ProvisionedThroughput={
                'ReadCapacityUnits': new_read_capacity,
                'WriteCapacityUnits': new_write_capacity
            }
        )

    def delete_table_with_name(self, table_name):
        print("Deleting DynamoDB table with name " + table_name)
        return self._client.delete_table(TableName=table_name)


class EC2:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.ec2 """

    def create_security_group(self):
        print("Creating RDS Security Group with name " + RDS_SECURITY_GROUP_NAME)
        return self._client.create_security_group(
            GroupName=RDS_SECURITY_GROUP_NAME,
            Description='RDS security group for public access',
            VpcId='vpc-1732737e'
        )

    def add_inbound_rule_to_sg(self, security_group_id):
        print("Adding inbound access rule to security group " + security_group_id)
        self._client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 5432,
                    'ToPort': 5432,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )


class RDS:

    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.rds """

    def create_postgresql_instance(self):
        print("Creating Amazon RDS PostgreSQL DB Instance...")

        security_group_id = self.create_db_security_group_and_add_rules()

        # create subnet group
        self.create_db_subnet_group()
        print("Creating DB Subnet group...")

        self._client.create_db_instance(
            DBName='MyPostgreSQLDB',
            DBInstanceIdentifier='mypostgresdb',
            DBInstanceClass='db.t2.micro',
            Engine='postgres',
            EngineVersion='9.6.6',
            Port=5432,
            MasterUsername='postgres',
            MasterUserPassword='mypostgrepassword',
            AllocatedStorage=20,
            MultiAZ=False,
            StorageType='gp2',
            PubliclyAccessible=True,
            VpcSecurityGroupIds=[security_group_id],
            DBSubnetGroupName=RDS_DB_SUBNET_NAME,
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'Niyazi-PostgreSQL-Instance'
                }
            ]
        )

    def describe_instances(self):
        print("Describing all RDS instances...")
        return self._client.describe_db_instances()

    def modify_master_user_password(self, db_identifier, new_password):
        print("Modifying master user password...")
        return self._client.modify_db_instance(
            DBInstanceIdentifier=db_identifier,
            MasterUserPassword=new_password
        )

    def take_backup_of_db_instance(self, db_identifier, db_snapshot_identifier, tags):
        print("Backing up DB instance...")
        return self._client.create_db_snapshot(
            DBInstanceIdentifier=db_identifier,
            DBSnapshotIdentifier=db_snapshot_identifier,
            Tags=tags
        )

    def restore_db_from_backup(self, db_identifier, db_snapshot_identifier):

        return self._client.restore_db_instance_from_db_snapshot(
            DBInstanceIdentifier=db_identifier,
            DBSnapshotIdentifier=db_snapshot_identifier
        )

    def delete_db(self, db_identifier):
        print("Deleting RDS instance with name " + db_identifier)
        return self._client.delete_db_instance(
            DBInstanceIdentifier=db_identifier,
            SkipFinalSnapshot=True
        )

    def create_db_subnet_group(self):
        print("Creating RDS DB Subnet Group " + RDS_DB_SUBNET_NAME)
        self._client.create_db_subnet_group(
            DBSubnetGroupName=RDS_DB_SUBNET_NAME,
            DBSubnetGroupDescription='My own subnet group for RDS DB',
            SubnetIds=['subnet-7c961507', 'subnet-35a27478', 'subnet-c31c74aa']
        )

    def create_db_security_group_and_add_rules(self):
        ec2_client = EC2Client().get_client()
        ec2 = EC2(ec2_client)

        # create security group
        security_group = ec2.create_security_group()

        # get id of the sg
        security_group_id = security_group['GroupId']

        print("Created RDS security group with id " + security_group_id)

        # add public access rule to sg
        ec2.add_inbound_rule_to_sg(security_group_id)

        print("Added inbound public access rule to sg with id " + security_group_id)

        return security_group_id


def get_rds():
    rds_client = RDSClient().get_client()
    rds = RDS(rds_client)
    return rds


def deploy_resources():
    rds_client = RDSClient().get_client()
    rds = RDS(rds_client)

    rds.create_postgresql_instance()

    print("Creating RDS PostgreSQL Instance...")


def describe_my_instances():
    print(str(get_rds().describe_instances()))


def modify_master_password():
    get_rds().modify_master_user_password('mypostgresdb', 'mybrandnewpassword')


def take_backup():
    tags = [{'Key': 'Name', 'Value': 'MyFirstSnapshot'}]
    get_rds().take_backup_of_db_instance('mypostgresdb', 'myveryfirstsnaphot', tags)


def restore_db():
    get_rds().restore_db_from_backup('mypostgresdbfromsnapshot', 'rds:mypostgresdb-2018-07-07-12-47')


def delete_db():
    get_rds().delete_db('mypostgresdbfromsnapshot')


def manage_rds_test_deployment():
    deploy_resources()
    # describe_my_instances()
    # modify_master_password()
    # take_backup()
    # restore_db()
    # delete_db()


def get_dynamodb():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)
    return dynamodb


def create_dynamodb_table():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)

    table_name = "Movies"

    # define attributes
    attribute_definitions = [
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ]

    # key schema definitions
    key_schema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  # Sort key
        }
    ]

    initial_iops = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    dynamodb_create_table_response = dynamodb.create_table(table_name, attribute_definitions, key_schema, initial_iops)
    print("Created DynamoDB Table named " + table_name + ":" + str(dynamodb_create_table_response))


def describe_table():
    print(str(get_dynamodb().describe_table("Movies")))


def update_table_iops():
    get_dynamodb().update_read_write_capacity("Movies", 10, 10)


def delete_table():
    get_dynamodb().delete_table_with_name("Movies")


def manage_dynamodb():
    create_dynamodb_table()
    # describe_table()
    # update_table_iops()
    # delete_table()

def get_dynamodb_client():
    dynamodb = boto3.client("dynamodb", region_name="eu-west-3", endpoint_url="http://localhost:8000")
    """ :type : pyboto3.dynamodb """
    return dynamodb


def get_dynamodb_resource():
    dynamodb = boto3.resource("dynamodb", region_name="eu-west-3", endpoint_url="http://localhost:8000")
    """ :type : pyboto3.dynamodb """
    return dynamodb


def create_table():
    table_name = "Movies"

    attribute_definitions = [
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ]

    key_schema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'
        }
    ]

    initial_iops = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }

    dynamodb_table_response = get_dynamodb_client().create_table(
        AttributeDefinitions=attribute_definitions,
        TableName=table_name,
        KeySchema=key_schema,
        ProvisionedThroughput=initial_iops
    )

    print("Created DynamoDB table:" + str(dynamodb_table_response))


def put_item_on_table():
    try:
        response = get_dynamodb_resource().Table("Movies").put_item(
            Item={
                'year': 2015,
                'title': "The Big New Movie",
                'info': {
                    'plot': "Nothing happens at all.",
                    'rating': decimal.Decimal(0)
                }
            }
        )

        print("A New Movie added to the collection successfully!")
        print(str(response))
    except Exception as error:
        print(error)


def update_item_on_table():
    response = get_dynamodb_resource().Table("Movies").update_item(
        Key={
            'year': 2015,
            'title': 'The Big New Movie'
        },
        UpdateExpression="set info.rating = :r, info.plot = :p, info.actors = :a",
        ExpressionAttributeValues={
            ':r': decimal.Decimal(3.5),
            ':p': "Everything happens all at once",
            ':a': ["Larry", "Moe", "David"]
        },
        ReturnValues="UPDATED_NEW"
    )

    print("Updating existing movie was success!")
    print(str(response))


def conditionally_update_an_item():
    try:
        respone = get_dynamodb_resource().Table("Movies").update_item(
            Key={
                'year': 2015,
                'title': 'The Big New Movie'
            },
            UpdateExpression="remove info.actors[0]",
            ConditionExpression="size(info.actors) >= :num",
            ExpressionAttributeValues={
                ':num': 3
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as error:
        if error.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(error.response['Error']['Message'])
        else:
            raise
    else:
        print("Updated item on table conditionally!")
        print(str(respone))


def get_item_on_table():
    try:
        response = get_dynamodb_resource().Table("Movies").get_item(
            Key={
                'year': 2015,
                'title': "The Big New Movie"
            }
        )
    except ClientError as error:
        print(error.response['Error']['Message'])
    else:
        item = response['Item']
        print("Got the item successfully!")
        print(str(response))


def delete_item_on_table():
    try:
        response = get_dynamodb_resource().Table("Movies").delete_item(
            Key={
                'year': 2015,
                'title': "The Big New Movie"
            }
        )
    except ClientError as error:
        if error.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(error.response['Error']['Message'])
        else:
            raise
    else:
        print("Deleted item successfully!")
        print(str(response))


def insert_sample_data():
    """
    [
        {
            "year": 2013,
            "title": "Rush",
            "info": {
                "directors": ["Ron Howard"],
                "release_date": "2013-09-02T00:00:00Z",
                "rating": 8.3,
                "genres": [
                    "Action",
                    "Biography",
                    "Drama",
                    "Sport"
                ],
                "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQyMDE0MTY0OV5BMl5BanBnXkFtZTcwMjI2OTI0OQ@@._V1_SX400_.jpg",
                "plot": "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.",
                "rank": 2,
                "running_time_secs": 7380,
                "actors": [
                    "Daniel Bruhl",
                    "Chris Hemsworth",
                    "Olivia Wilde"
                ]
            }
        }
    ]
    """
    table = get_dynamodb_resource().Table("Movies")

    with open("moviedata.json") as json_file:
        movies = json.load(json_file, parse_float=decimal.Decimal)
        for movie in movies:
            year = int(movie['year'])
            title = movie['title']
            info = movie['info']

            print("Adding movie:", year, title)

            table.put_item(
                Item={
                    'year': year,
                    'title': title,
                    'info': info
                }
            )

    print("Sample movie data inserted successfully!")


def query_movies_released_in_1985():
    response = get_dynamodb_resource().Table("Movies").query(
        KeyConditionExpression=Key('year').eq(1985)
    )

    for movie in response['Items']:
        print(movie['year'], ":", movie['title'])


def query_movies_with_extra_conditions():
    print("Movies from 1992 - title A-L, with genres and lead actor")

    response = get_dynamodb_resource().Table("Movies").query(
        ProjectionExpression="#yr, title, info.genres, info.actors[0]",
        ExpressionAttributeNames={"#yr": "year"},
        KeyConditionExpression=Key('year').eq(1992) & Key('title').between('A', 'L')
    )

    for movie in response['Items']:
        print(str(movie))


def scan_whole_table_for_items():
    filter_expression = Key('year').between(1950, 1959)
    projection_expression = "#yr, title, info.rating"
    ean = {"#yr": "year",}

    response = get_dynamodb_resource().Table("Movies").scan(
        FilterExpression=filter_expression,
        ProjectionExpression=projection_expression,
        ExpressionAttributeNames=ean
    )

    for movie in response['Items']:
        print(str(movie))


def manage_dynamodb():
    # create_table()
    # put_item_on_table()
    # update_item_on_table()
    # conditionally_update_an_item()
    # get_item_on_table()
    # delete_item_on_table()
    # insert_sample_data()
    # query_movies_released_in_1985()
    # query_movies_with_extra_conditions()
    scan_whole_table_for_items()


def config(filename=DB_CONFIG_FILE, section='postgresql'):
    # create a parser
    parser = ConfigParser()

    #read the configuration
    parser.read(filename)

    # get the section
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0] not found in the {1} file', format(section, filename))
    return db


def connect_to_rds():
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the postgresql database
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print("PostgreSQL Database Version:")
        cur.execute('SELECT version()')

        # fetch the data
        db_version = cur.fetchone()
        print(db_version)

        # close the connection
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')


def create_tables():
    # provide sql statements
    commands = (
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL
        ) 
        """,
        """
        CREATE TABLE accounts (
            account_id SERIAL PRIMARY KEY,
            account_name VARCHAR(255) NOT NULL
        )
        """
    )

    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # execute commands one by one
        for command in commands:
            cur.execute(command)

        cur.close()

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_vendor_list(user_list):

    sql = "INSERT INTO users(user_name) VALUES (%s)"
    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.executemany(sql, user_list)

        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_users():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT user_id, user_name FROM users ORDER BY user_name")
        print("Numbers of users:", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_user(user_id, user_name):
    sql = """ UPDATE users
              SET user_name = %s 
              WHERE user_id = %s """

    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_name, user_id))

        updated_rows = cur.rowcount

        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def delete_user(user_id):

    conn = None
    rows_deleted = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))

        rows_deleted = cur.rowcount

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows_deleted


def sql_with_rds():
    # connect_to_rds()
    # create_tables()

    # insert_vendor_list([
    #     ('John Doe',),
    #     ('Douglas Smith',),
    #     ('Anthony Jenkins',),
    #     ('David Salazar',),
    #     ('Richard Forrester',),
    #     ('Shawn Reddick',),
    #     ('Philip Broyles',)
    # ])

    get_users()

    #response = update_user(1, 'Niyazi')
    #print(response)

    delete_user(1)

    get_users()


def create_db_subnet_group():
    rds_client = boto3.client("rds", region_name="eu-west-3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    print("Creating RDS DB Subnet Group " + RDS_DB_SUBNET_GROUP)
    rds_client.create_db_subnet_group(
        DBSubnetGroupName=RDS_DB_SUBNET_GROUP,
        DBSubnetGroupDescription="My own db subnet group",
        SubnetIds=['subnet-e086bfaa', 'subnet-12f6ec6a', 'subnet-979958fe']
    )


def create_db_security_group_and_add_inbound_rule():
    ec2 = boto3.client("ec2", region_name="eu-west-3")
    """ :type : pyboto3.ec2 """

    # create security group
    security_group = ec2.create_security_group(
        GroupName="my-rds-public-sg",
        Description="RDS security group to allow public access",
        VpcId="vpc-a25693cb"
    )

    # get id of the
    security_group_id = security_group['GroupId']

    print("Created RDS security group with id " + security_group_id)

    # add public access rule to sg
    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 5432,
                'ToPort': 5432,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
    )

    print("Added inbound access rule to security group with id " + security_group_id)
    return security_group_id


def launch_rds_instance():
    rds_client = boto3.client("rds", region_name="eu-west-3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    print("Launching AWS RDS PostgreSQL instance...")
    security_group_id = create_db_security_group_and_add_inbound_rule()

    create_db_subnet_group()
    print("Created DB Subnet Group")

    rds_client.create_db_instance(
        DBName='PostgreSQLDBInstance',
        DBInstanceIdentifier="postgresqlinstanceidentifier",
        DBInstanceClass="db.t2.micro",
        Engine="postgres",
        EngineVersion="9.6.6",
        Port=5432,
        MasterUsername="postgres",
        MasterUserPassword="mypostgrespassword",
        AllocatedStorage=20,
        MultiAZ=False,
        StorageType="gp2",
        PubliclyAccessible=True,
        VpcSecurityGroupIds=[security_group_id],
        DBSubnetGroupName=RDS_DB_SUBNET_GROUP
    )


def eb_get_info(region="us-east-1"):
    """
    {
        'EnvironmentName': 'Movieapi-env', 
        'EnvironmentId': 'e-4neb2hjgqp', 
        'ApplicationName': 'movie-api', 
        'VersionLabel': 'Sample Application', 
        'SolutionStackName': '64bit Amazon Linux 2 v3.4.5 running Ruby 3.0', 
        'PlatformArn': 'arn:aws:elasticbeanstalk:us-east-1::platform/Ruby 3.0 running on 64bit Amazon Linux 2/3.4.5', 
        'EndpointURL': 'awseb-AWSEB-1GP6WIDMVMTGH-1008250489.us-east-1.elb.amazonaws.com', 
        'CNAME': 'Movieapi-env.eba-cmxgxpqk.us-east-1.elasticbeanstalk.com', 
        'DateCreated': datetime.datetime(2022, 5, 4, 2, 50, 12, 283000, tzinfo=tzutc()), 
        'DateUpdated': datetime.datetime(2022, 5, 4, 2, 53, 32, 613000, tzinfo=tzutc()), 
        'Status': 'Ready', 
        'AbortableOperationInProgress': False, 
        'Health': 'Green', 
        'HealthStatus': 'Ok', 
        'Tier': {
            'Name': 'WebServer', 
            'Type': 'Standard', 
            'Version': '1.0'
        }, 
        'EnvironmentLinks': [], 
        'EnvironmentArn': 'arn:aws:elasticbeanstalk:us-east-1:146669583780:environment/movie-api/Movieapi-env'
    }
    status = eb_get_info()
    stat = status.get('Status', 'dont know')
    """
    kembali = None
    try:
        client = boto3.client('elasticbeanstalk', region,
                            aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        response = client.describe_environments()
        for index, item in enumerate(response['Environments']):
            print(index+1, item)
            kembali = item
    except:
        raise

    return kembali


def delete_eb3_application(region="us-east-1", ApplicationName='movie-api'):
    """
    Unable to delete application movie-api because it has a version that is deployed to a running environment.
    """
    client = boto3.client('elasticbeanstalk', region,
                          aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    # response = client.delete_environment_configuration(
    #     ApplicationName=ApplicationName,
    #     EnvironmentName=EnvironmentName
    # )
    response = client.delete_application(
        ApplicationName=ApplicationName
    )
    print(response)


def delete_eb3_configuration(region="us-east-1", EnvironmentName='Movieapi-env', ApplicationName='movie-api'):
    """
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application
    {
        'ResponseMetadata': {
            'RequestId': '4d17b537-4f1a-48ed-b9b5-e6cdd4d49670', 
            'HTTPStatusCode': 200, 
            'HTTPHeaders': {
                'content-type': 'text/xml', 
                'date': 'Wed, 04 May 2022 07:23:18 GMT', 
                'x-amzn-requestid': '4d17b537-4f1a-48ed-b9b5-e6cdd4d49670', 
                'content-length': '253', 
                'connection': 'keep-alive'
            }, 
            'RetryAttempts': 0
        }
    }
    """
    client = boto3.client('elasticbeanstalk', region,
                          aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = client.delete_environment_configuration(
        ApplicationName=ApplicationName,
        EnvironmentName=EnvironmentName
    )
    print(response)


def terminate_eb3_environment(region="us-east-1", EnvironmentName='Movieapi-env', EnvironmentId='e-4neb2hjgqp'):
    """
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application
    {
        'EnvironmentName': 'Movieapi-env', 
        'EnvironmentId': 'e-4neb2hjgqp', 
        'ApplicationName': 'movie-api', 
        'SolutionStackName': '64bit Amazon Linux 2 v3.4.5 running Ruby 3.0', 
        'PlatformArn': 'arn:aws:elasticbeanstalk:us-east-1::platform/Ruby 3.0 running on 64bit Amazon Linux 2/3.4.5', 
        'EndpointURL': 'awseb-AWSEB-1GP6WIDMVMTGH-1008250489.us-east-1.elb.amazonaws.com', 
        'CNAME': 'Movieapi-env.eba-cmxgxpqk.us-east-1.elasticbeanstalk.com', 
        'DateCreated': datetime.datetime(2022, 5, 4, 2, 50, 12, 283000, tzinfo=tzutc()), 
        'DateUpdated': datetime.datetime(2022, 5, 4, 7, 30, 10, 8000, tzinfo=tzutc()), 
        'Status': 'Terminating', 
        'AbortableOperationInProgress': False, 
        'Health': 'Grey', 
        'Tier': {'Name': 'WebServer', 'Type': 'Standard', 'Version': '1.0'}, 
        'EnvironmentArn': 'arn:aws:elasticbeanstalk:us-east-1:146669583780:environment/movie-api/Movieapi-env', 
        'ResponseMetadata': {
            'RequestId': '4535c0c5-4ffc-462c-83c1-10211c3a7f37', 
            'HTTPStatusCode': 200, 
            'HTTPHeaders': {
                'content-type': 'text/xml', 
                'date': 'Wed, 04 May 2022 07:30:09 GMT', 
                'x-amzn-requestid': '4535c0c5-4ffc-462c-83c1-10211c3a7f37', 
                'content-length': '1313', 
                'connection': 'keep-alive'
            }, 
            'RetryAttempts': 0
        }
    }
    """
    client = boto3.client('elasticbeanstalk', region,
                          aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    # response = client.delete_environment_configuration(
    #     ApplicationName=ApplicationName,
    #     EnvironmentName=EnvironmentName
    # )
    response = client.terminate_environment(
        EnvironmentId=EnvironmentId,
        EnvironmentName=EnvironmentName,
        TerminateResources=True,
        ForceTerminate=True
    )
    print(response)


def get_rds_databases():
    """
    database-1 db.t3.micro 100 postgres
    """
    client = boto3.client(
        'rds', 'us-east-1', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = client.describe_db_instances()
    for i in response['DBInstances']:
        db_name = i['DBName']
        db_instance_name = i['DBInstanceIdentifier']
        db_type = i['DBInstanceClass']
        db_storage = i['AllocatedStorage']
        db_engine = i['Engine']
        print(db_instance_name, db_type, db_storage, db_engine)


def get_rds_databases_simple():
    client = boto3.client('rds', 'us-east-1', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    # response = client.describe_db_instances(Filters=[{'Name': 'string','Values': ['string',]}])
    response = client.describe_db_instances()
    for instance in response ["DBInstances"]:
        print (instance['DBInstanceIdentifier'])
        # response = client.delete_db_instance(DBInstanceIdentifier=instance['DBInstanceIdentifier'])
        # SkipFinalSnapshot=True
        # DeleteAutomatedBackups=True


def delete_rds_databases():
    """
    {
        'DBInstance': {
            'DBInstanceIdentifier': 'database-1', 
            'DBInstanceClass': 'db.t3.micro', 
            'Engine': 'postgres', 
            'DBInstanceStatus': 'deleting', 
            'MasterUsername': 'postgres', 
            'DBName': 'movie_api_db', 
            'Endpoint': {'Address': 'database-1.ckmp4dqdok19.us-east-1.rds.amazonaws.com', 'Port': 5432, 'HostedZoneId': 'Z2R2ITUGPM61AM'}, 
            'AllocatedStorage': 100, 
            'InstanceCreateTime': datetime.datetime(2022, 5, 4, 2, 16, 44, 854000, tzinfo=tzutc()), 
            'PreferredBackupWindow': '06:24-06:54', 
            'BackupRetentionPeriod': 7, 
            'DBSecurityGroups': [], 
            'VpcSecurityGroups': [
                {'VpcSecurityGroupId': 'sg-072ac00cdcc8a039e', 'Status': 'active'}
            ], 
            'DBParameterGroups': [
                {'DBParameterGroupName': 'default.postgres12', 'ParameterApplyStatus': 'in-sync'}
            ], 
            'AvailabilityZone': 'us-east-1f', 
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'default-vpc-0d85e7324a1cc3495', 
                'DBSubnetGroupDescription': 'Created from the RDS Management Console', 
                'VpcId': 'vpc-0d85e7324a1cc3495', 
                'SubnetGroupStatus': 'Complete', 
                'Subnets': [
                    {'SubnetIdentifier': 'subnet-0d3c87f7b761e44bb', 'SubnetAvailabilityZone': {'Name': 'us-east-1b'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, 
                    {'SubnetIdentifier': 'subnet-0aae6dfda3ae7e735', 'SubnetAvailabilityZone': {'Name': 'us-east-1a'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, 
                    {'SubnetIdentifier': 'subnet-0cb84a3f95e6346a9', 'SubnetAvailabilityZone': {'Name': 'us-east-1f'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, 
                    {'SubnetIdentifier': 'subnet-0e0ebe944941d3c8f', 'SubnetAvailabilityZone': {'Name': 'us-east-1c'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, 
                    {'SubnetIdentifier': 'subnet-021fe07a1621c55ae', 'SubnetAvailabilityZone': {'Name': 'us-east-1e'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, 
                    {'SubnetIdentifier': 'subnet-06be7bc2ad7fac6b9', 'SubnetAvailabilityZone': {'Name': 'us-east-1d'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}]
            }, 
            'PreferredMaintenanceWindow': 'sat:07:50-sat:08:20', 
            'PendingModifiedValues': {}, 
            'LatestRestorableTime': datetime.datetime(2022, 5, 4, 7, 4, 31, tzinfo=tzutc()), 
            'MultiAZ': False, 
            'EngineVersion': '12.10', 
            'AutoMinorVersionUpgrade': True, 
            'ReadReplicaDBInstanceIdentifiers': [], 
            'LicenseModel': 'postgresql-license', 
            'OptionGroupMemberships': [{'OptionGroupName': 'default:postgres-12', 'Status': 'in-sync'}], 
            'PubliclyAccessible': True, 
            'StorageType': 'gp2', 
            'DbInstancePort': 0, 
            'StorageEncrypted': True, 
            'KmsKeyId': 'arn:aws:kms:us-east-1:146669583780:key/d86a206f-e70e-41e2-bf14-df1603d75c33', 
            'DbiResourceId': 'db-WD5NED5HL7LVDTJOIE55M6ZEUM', 
            'CACertificateIdentifier': '', 
            'DomainMemberships': [], 
            'CopyTagsToSnapshot': True, 
            'MonitoringInterval': 0, 
            'DBInstanceArn': 'arn:aws:rds:us-east-1:146669583780:db:database-1', 
            'IAMDatabaseAuthenticationEnabled': False, 
            'PerformanceInsightsEnabled': True, 
            'PerformanceInsightsKMSKeyId': 'arn:aws:kms:us-east-1:146669583780:key/d86a206f-e70e-41e2-bf14-df1603d75c33', 
            'PerformanceInsightsRetentionPeriod': 7, 
            'DeletionProtection': False, 
            'AssociatedRoles': [], 
            'MaxAllocatedStorage': 1000, 
            'TagList': [], 
            'CustomerOwnedIpEnabled': False, 
            'BackupTarget': 'region'
        }, 
        'ResponseMetadata': {
            'RequestId': '3852f685-8348-4108-9b0b-598373132f2d', 
            'HTTPStatusCode': 200, 
            'HTTPHeaders': {
                'x-amzn-requestid': '3852f685-8348-4108-9b0b-598373132f2d', 
                'content-type': 'text/xml', 
                'content-length': '5757', 
                'date': 'Wed, 04 May 2022 07:11:53 GMT'
            }, 
            'RetryAttempts': 0
        }
    }
    """
    client = boto3.client('rds', 'us-east-1', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    # response = client.describe_db_instances(Filters=[{'Name': 'string','Values': ['string',]}])
    response = client.describe_db_instances()
    for instance in response ["DBInstances"]:
        print (instance['DBInstanceIdentifier'])
        yn = input(f"Delete {instance['DBInstanceIdentifier']}? y[n] ")
        if yn.lower() == 'y':
            response = client.delete_db_instance(DBInstanceIdentifier=instance['DBInstanceIdentifier'], SkipFinalSnapshot=True, DeleteAutomatedBackups=True)
            print(response)


def ec2_regions():
    """
    eu-north-1
    ap-south-1
    eu-west-3
    eu-west-2
    eu-west-1
    ap-northeast-3
    ap-northeast-2
    ap-northeast-1
    sa-east-1
    ca-central-1
    ap-southeast-1
    ap-southeast-2
    eu-central-1
    us-east-1
    us-east-2
    us-west-1
    us-west-2
    """
    ec2 = boto3.client('ec2', 'us-east-1', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    regions = ec2.describe_regions().get('Regions',[] )
    for region in regions:
        print(region['RegionName'])


def sample_oprek():
    """
    EB: terminate, hapus, buktikan dah gak ada
    """

    input('siap2 terminate... ')
    terminate_eb3_environment()

    tunggu = True
    while tunggu:
        status = eb_get_info()
        yn = input(f"[{status.get('Status', 'donno...')}] tunggu dari terminating ke terminated? ")
        if yn.lower() != 'y':
            tunggu = False

    input('siap2 hapus... ')
    delete_eb3_application()

    input('mungkin ini akan error, krn di atas sudah hapus app... ')
    delete_eb3_configuration()

    print('sudah selesai hapus, lihat now utk terakhir kali...')
    eb_get_info()


def set_env():
    """
    untested...
    https://stackoverflow.com/questions/66519659/aws-eb-setenv-in-boto3-python
    """
    client = boto3.client("elasticbeanstalk")

    client.update_environment(
        ApplicationName="my-app",
        EnvironmentName="my-env",
        OptionSettings=[
            {
                "Namespace": "aws:elasticbeanstalk:application:environment",
                "OptionName": "my-env-variable",
                "Value": "my-value",
            }
        ]
    )


def listen_sqs():
    while True:
        sqs = boto3.client('sqs')
        response = sqs.receive_message(QueueUrl=SQS_QUEUE_URL,
                                       MaxNumberOfMessages=1,
                                       MessageAttributeNames=['All'],
                                       VisibilityTimeout=1,
                                       WaitTimeSeconds=0)
        if 'Messages' in response:
            message = response['Messages'][0]
            body = message['Body']
            print("Message received: \n\n{0}\n".format(message))
            sqs.delete_message(
                QueueUrl=SQS_QUEUE_URL,
                ReceiptHandle=message['ReceiptHandle']
            )
            print('Message deleted!')
        sys.stdout.flush()
        time.sleep(10)
