from schnell.app.aws.iam import iam
from schnell.app.aws.ec2 import ec2
from schnell.app.aws.rds import rds
from schnell.app.aws.vpc import vpc
from schnell.app.aws.ebs import ebs
from schnell.app.aws.lambada import lambada
from schnell.app.aws.cloudformation import cf
from schnell.app.aws.kafka import kafka
from schnell.app.printutils import pp
import time


def handle_iam(request):
    """
    roles/list
    users/list
    users/detail/uid
    policies/list
    groups/list
    profiles/list
    accesskeys/list/username
    """    
    jenis, sisa = request.split('/', 1)
    if jenis == 'roles':
        if sisa == 'list':
            print('[cloudia] roles/read-list...')
            iam.list_roles_resource()
        elif sisa .startswith('detail'):
            '''
            /aws)iam/roles/detail/rolename
            '''
            rolename = sisa.removeprefix('detail/')
            iam.describe_role(rolename)
        elif sisa.startswith('+'):
            '''
            /aws)iam/roles/+/newrolename
            '''
            rolename = sisa.removeprefix('+/')
            iam.create_role(rolename)
        elif sisa.startswith('-'):
            '''
            /aws)iam/roles/-/rolename
            '''
            rolename = sisa.removeprefix('-/')
            iam.delete_role_resource(rolename)
    elif jenis == 'users':
        if sisa == 'list':
            print('[cloudia] users/list...')
            iam.list_users_resource()
        elif sisa .startswith('detail'):
            '''
            /aws)iam/users/detail/0
            '''
            sisa2 = sisa.removeprefix('detail/')
            if sisa2 == '0':
                print('[cloudia] users/detail/0...')
                iam.describe_user()
    elif jenis == 'policies':
        if sisa .startswith('list'):
            print('[cloudia] policies/list...')
            filter = sisa.removeprefix('list')
            if filter.startswith('/'):
                '''
                /aws)iam/policies/list
                '''
                filter = filter.removeprefix('/')
                iam.list_policies_resource(filter)
            else:
                '''
                /aws)iam/policies/list/administrator
                '''
                iam.list_policies_resource()
    elif jenis == 'groups':
        if sisa == 'list':
            print('[cloudia] groups/list...')
            iam.list_groups_resource()
        elif sisa.startswith('+'):
            '''
            /aws)iam/groups/+/newgroups
            '''
            groupname = sisa.removeprefix('+/')
            iam.create_group(groupname)
        elif sisa.startswith('-'):
            '''
            /aws)iam/groups/-/groupname
            '''
            groupname = sisa.removeprefix('-/')
            iam.delete_group_resource(groupname)
    elif jenis == 'profiles':
        if sisa == 'list':
            print('[cloudia] profiles/list...')
            iam.list_instance_profile_resource()
    elif jenis == 'accesskeys':
        if sisa .startswith('list'):
            print('[cloudia] accesskeys/list...')
            username = sisa.removeprefix('list/')
            iam.list_access_keys(username)


def handle_rds(request):
    """
    fm/
        /aws)rds/
            all
            list
    """
    if request == 'all':
        # menghasilkan
        print('[cloudia] rds/all...')
        instances = rds.describe_all_instances()
        pp(instances)
        return
    elif request == 'list':
        # kosong
        print('[cloudia] rds/list...')
        # instances = rds.list_databases()
        # pp(instances)
        rds.list_databases()
        return

    # jenis, sisa = request.split('/', 1)

def handle_subnet(request):
    """
    /aws)subnet/list
    /aws)subnet/list/vpcid
    """
    if request.startswith('list'):
        if request == 'list':
            '''
            all subnets
            /aws)subnet/list
            '''
            ec2.describe_subnets()
        elif request == 'list2':
            '''
            all subnets
            /aws)subnet/list2
            '''
            vpc.list_subnets()
        else:
            '''
            subnets owned by vpc
            /aws)subnet/list/vpcid
            '''
            vpcid = request.removeprefix('list/')
            ec2.describe_subnets(vpcid)
        return

    jenis, sisa = request.split('/', 1)
    if jenis == '+':
        '''
        create subnet of vpc
        /aws)subnet/+/vpcid/cidrsubnet
        /aws)subnet/+/cidrvpc,cidrsubnet
        '''
        if sisa.count('/')==1:
            vpcid,cidrsubnet=sisa.split('/')
            vpc.create_subnet_of_vpc(cidrvpc, cidrsubnet)
        elif sisa.count(',')==1:
            cidrvpc,cidrsubnet=sisa.split(',')
            vpc.create_vpc_then_subnet(cidrvpc, cidrsubnet)
    elif jenis == '-':
        '''
        /aws)subnet/-/subnetid
        '''
        subnetid = sisa
        vpc.delete_subnet(subnetid)
    elif jenis == 'detail':
        '''
        /aws)subnet/detail/subnetid
        '''
        subnetid = sisa
        ec2.detail_subnet(subnetid)
    elif jenis == 'cidr':
        '''
        /aws)subnet/cidr/cidrprefix
        '''
        cidrprefix = sisa
        ec2.subnets_by_cidr(cidrprefix)


def handle_vpc(request):
    """
    fm/
        /aws)vpc/
            list
            +
            -/vpcid
            0
                utk dapatkan default vpc, fm//aws)vpc/0 -> utk tau gimana responsenya, dan get vpcid nya
            detail/vpcid
    """
    if request == 'list':
        # /aws)vpc/list
        print('[cloudia] vpc/list...')
        # instances = rds.list_databases()
        # pp(instances)
        vpc.list_vpcs()
        return
    elif request == '+':
        # /aws)vpc/+
        vpc.create_default_vpc()
        return
    elif request == '0':
        # /aws)vpc/0
        res = vpc.get_default_first_vpc()
        pp(res)
        return

    jenis, sisa = request.split('/', 1)
    if jenis == '-':
        vpc.delete_vpc(sisa)
    elif request == '+':
        '''
        /aws)vpc/+/vpcsubnet/cidrvpc/cidrsubnet
        '''
        if sisa.startswith('vpcsubnet'):
            cidrvpc,cidrsubnet=sisa.removeprefix('vpcsubnet/').split('/')
            vpc.create_vpc_then_subnet(cidrvpc,cidrsubnet)
        
    elif jenis == 'detail':
        # /aws)vpc/detail/vpcid
        vpc.describe_vpc(sisa)


def handle_ebs(request):
    """
    fm/
        /aws)ebs/
            list
            list/my-env
            vol/list
            vol/-
            vol/-/volid
    """
    if request == 'list':
        print('[cloudia] ebs/list...')
        instances = ebs.describe_environments()
        pp(instances)
        # ebs.describe_environments()
        return
    elif request == 'info':
        print('[cloudia] ebs/info...')
        ebs.get_info()
        return
    jenis, sisa = request.split('/', 1)
    if jenis == 'vol':
        if sisa == 'list':
            # not working
            vols = ebs.list_volumes_resource()

        if sisa .startswith ('+'):
            # /aws)ebs/+/name=volname,type=gp2,size=10
            items = sisa.removeprefix('+/').split(',')
            kwargs = {}
            for item in items:
                k,v = item.split('=')
                if k == 'name':
                    kwargs.update({
                        'volume_name': v,
                    })
                elif k == 'size':
                    kwargs.update({
                        'size': v,
                    })
                elif k == 'type':
                    kwargs.update({
                        'volume_type': v,
                    })
                # elif k == 'sg':
                #     kwargs.update({
                #         'SECURITY_GROUP_ID': v,
                #     })
                # elif k == 'sn':
                #     kwargs.update({
                #         'SUBNET_ID': v,
                #     })
                # elif k == 'num': # instances max count
                #     kwargs.update({
                #         'jumlah': int(v),
                #     })
            ec2.create_volume_resource(**kwargs)

        elif sisa .startswith('-'):
            '''
            vol/-
            vol/-/volid
            '''
            if sisa == '-':
                ebs.delete_unused_volumes()
            else:
                volid = sisa.removeprefix('-')
                ebs.delete_volume_byid(volid)

        elif sisa .startswith('detail'):
            '''
            vol/detail/volid
            '''
            volid = sisa.removeprefix('detail/')
            ebs.describe_volumes(volid)


def handle_lambda(request):
    if request == 'list':
        # /aws)lambda/list
        print('[cloudia] lambda/list...')
        instances = lambada.list_function()
        pp(instances)
        return
    if request == 'info':
        # /aws)lambda/info
        print('[cloudia] lambda/info...')
        instances = lambada.info()
        pp(instances)
        return
    if '/' in request:
        jenis, sisa = request.split('/', 1)
    else:
        jenis = request
        sisa = ''
    if jenis == '+':
        # /aws)lambda/+/name=wiekes-lambda,zip=lambda.zip,handler=handler.handler,role=wiekes-lambda
        items = sisa.split(',')
        kwargs = {}
        for item in items:
            k,v = item.split('=')
            if k == 'name':
                kwargs.update({
                    'name': v,
                })
            elif k == 'zip':
                kwargs.update({
                    'zipfilepath': v,
                })
            elif k == 'handler':
                kwargs.update({
                    'handler_filefunc': v,
                })
            elif k == 'role':
                kwargs.update({
                    'role_name': v,
                })
        lambada.create_function(**kwargs)
    elif jenis == '++':
        '''
        create zip (berisi lambda.py dg handler func) yg ready to deploy
        /aws)lambda/++
        /aws)lambda/++/lambda.zip
        '''
        if not sisa.strip():
            lambada.create_handler()
        else:
            lambada.create_handler(sisa.strip())
    elif jenis == '+++':
        '''
        create_iamrole_then_handler_then_function(function_name='helloWorldLambda', 
            output_filename='lambda.zip',
            role_name='lambda-role',
            handler_filefunc='lambda.lambda_handler')
        /aws)lambda/+++/name=wiekes-lambda-1,role=wiekes-iam-role-1,out=lambda.zip,handler=lambda.handler
        name, role, out, handler
        '''
        items = sisa.split(',')
        kwargs = {}
        for item in items:
            k,v = item.split('=')
            if k == 'name':
                kwargs.update({
                    'function_name': v,
                })
            elif k == 'role':
                kwargs.update({
                    'role_name': v,
                })
            elif k == 'out':
                kwargs.update({
                    'output_filename': v,
                })
            elif k == 'handler':
                kwargs.update({
                    'handler_filefunc': v,
                })
        lambada.create_iamrole_then_handler_then_function(**kwargs)
    elif jenis == 'detail':
        # /aws)lambda/detail/funcname
        funcname = sisa
        lambada.describe_function(funcname)
    elif jenis == 'invoke':
        '''
        /aws)lambda/invoke/funcname
        /aws)lambda/invoke/funcname/stringdictargs
        play around dulu dg stringdictargs
        {1:"satu",2:"dua"}
        '''
        funcname = sisa
        if '/' in sisa:
            funcname, stringdictargs = sisa.split('/')
            resp = lambada.invoke_function(funcname, eval(stringdictargs))
        else:
            resp = lambada.invoke_function(funcname)
    elif jenis == '-': 
        # /aws)lambda/-/funcname
        funcname = sisa
        lambada.delete_function(funcname)
        # time.sleep(3) # tunggu 3 detik
        # ec2.terminate_instance(instance_id)

def handle_ec2(request):
    """
    fm/
        /aws)ec2/
            list
            +/name=...,ami=...,jumlah=...,kp=...,sg=...,sn=...,
            detail/instance-id
            kp/list
            kp/+keypairname
            sg/list
            sg/d/<sg id>
            sn/list
            ip/list
    """
    if request == 'list':
        # /aws)ec2/list
        print('[cloudia] ec2/list...')
        instances = ec2.list_instances()
        # pp(instances)
        # ebs.describe_environments()
        return
    elif request == 'test':
        # ec2.current_test(instance_id = 'i-000690c7d24e0fe9a', KEY_PAIR_NAME = 'mysidoarjokeypair', alamat_host = 'ec2-54-145-223-160.compute-1.amazonaws.com')
        ec2.current_test(alamat_host = 'ec2-54-145-223-160.compute-1.amazonaws.com', commands='pwd && uname -a && df')
        return

    jenis, sisa = request.split('/', 1) # kp/list, etc
    if jenis == '+':
        # /aws)ec2/+/name=wiekes-ec2,ami=ami-0c4f7023847b90238
        items = sisa.split(',')
        # create_instances(self, 
        # num           jumlah=1, 
        # name          instance_name='my-ec2-instance', 
        # ami           AMI_ID='ami-0c02fb55956c7d316', 
        #               INSTANCE_PROFILE=None, 
        # kp            KEY_PAIR_NAME=None, 
        # sg            SECURITY_GROUP_ID=None, 
        # sn            SUBNET_ID=None):
        kwargs = {}
        for item in items:
            k,v = item.split('=')
            if k == 'name':
                kwargs.update({
                    'instance_name': v,
                })
            elif k == 'ami':
                kwargs.update({
                    'AMI_ID': v,
                })
            elif k == 'kp':
                kwargs.update({
                    'KEY_PAIR_NAME': v,
                })
            elif k == 'sg':
                kwargs.update({
                    'SECURITY_GROUP_ID': v,
                })
            elif k == 'sn':
                kwargs.update({
                    'SUBNET_ID': v,
                })
            elif k == 'num': # instances max count
                kwargs.update({
                    'jumlah': int(v),
                })
        ec2.create_instances(**kwargs)
    elif jenis == '++':
        # simpan keypairfile utk ssh + ssh
        # /aws)ec2/++/name=wiekes-ec2,ami=ami-0c4f7023847b90238,kp=mysidoarjokeypair,cmd=pwd && hostname
        items = sisa.split(',')
        kwargs = {}
        for item in items:
            k,v = item.split('=')
            if k == 'name':
                kwargs.update({
                    'instance_name': v,
                })
            elif k == 'ami':
                kwargs.update({
                    'AMI_ID': v,
                })
            elif k == 'kp':
                kwargs.update({
                    'KEY_PAIR_NAME': v,
                })
            elif k == 'sg':
                kwargs.update({
                    'SECURITY_GROUP_ID': v,
                })
            elif k == 'sn':
                kwargs.update({
                    'SUBNET_ID': v,
                })
            elif k == 'num': # instances max count
                kwargs.update({
                    'jumlah': int(v),
                })
            elif k == 'cmd': # instances max count
                kwargs.update({
                    'commands': v,
                })
        ec2.create_instance_until_ssh(**kwargs)
    elif jenis == 'detail':
        # /aws)ec2/detail/i-061148269d4bcff40
        instance_id = sisa
        ec2.describe_instances(instance_id)
    elif jenis == 'terminate':
        # /aws)ec2/terminate/i-061148269d4bcff40
        instance_id = sisa
        ec2.terminate_instance(instance_id)
    elif jenis == 'stop': 
        # /aws)ec2/stop/i-061148269d4bcff40
        instance_id = sisa
        ec2.stop_instance(instance_id)
    elif jenis == '-': 
        # /aws)ec2/-/i-061148269d4bcff40
        instance_id = sisa
        ec2.stop_instance(instance_id)
        time.sleep(3) # tunggu 3 detik
        ec2.terminate_instance(instance_id)
    elif jenis == 'kp':
        '''
        fm//aws)ec2/kp/list
        fm//aws)ec2/kp/detail/kp-wiekegaia
        '''
        if sisa == 'list': 
            # /aws)ec2/kp/list
            ec2.list_ssh_keys()
        elif sisa.startswith('detail'):
            # /aws)ec2/kp/detail/kpname
            keypairname = sisa.removeprefix('detail/').strip()
            ec2.search_ssh_keys(keypairname)
        elif sisa.startswith('+'):
            # /aws)ec2/kp/+mysidoarjokeypair
            # /aws)ec2/kp/++mysidoarjokeypair
            keypairname = sisa.removeprefix('+').strip()
            if keypairname.startswith('+'):
                keypairname = keypairname.removeprefix('+').strip()
                ec2.create_key_pair(keypairname)
            else:
                ec2.create_ssh_keys(keypairname)
        elif sisa.startswith('-'):
            # /aws)ec2/kp/-mysidoarjokeypair
            keypairname = sisa.removeprefix('-').strip()
            ec2.delete_ssh_keys(keypairname)
    elif jenis == 'sg':
        '''
        /aws)ec2/sg
            /list
            /detail/sgid
            /-/sgid
            /attach/sgid/instanceid
            /detach/sgid/instanceid
            /ssh/+/vpcid
        buat sg/ssh menerima vpcid
        /aws)ec2/sg/ssh/+/vpcid
        sg/ssh kita bilang, "common group"
        '''
        if sisa == 'list': 
            '''
            /aws)ec2/sg/list
            '''
            ec2.list_security_groups()
        elif sisa.startswith('detail/'):
            '''
            /aws)ec2/sg/detail/<sg id>
            '''
            sg_id = sisa.removeprefix('detail/')
            ec2.describe_security_group(sg_id)
        elif sisa.startswith('-'):
            '''
            hapus sg
            /aws)ec2/sg/-/sgid
            def delete_security_group(self, SECURITY_GROUP_ID = 'sg-0e0fe09d642656bf3'):
            '''
            sgid = sisa.removeprefix('-')
            ec2.delete_security_group(sgid)
        elif sisa.startswith('attach'):
            '''
            /attach/sgid/instanceid
            def attach_security_group_to_instance(self, SECURITY_GROUP_ID = 'sg-084dfa143cc85a5cf', INSTANCE_ID = 'i-04091b10d2cdc86aa'):
            '''
            attach, sgid, iid = sisa.split('/')
            ec2.attach_security_group_to_instance(sgid, iid)
        elif sisa.startswith('detach'):
            '''
            /detach/sgid/instanceid
            def detach_security_group_to_instance(self, SECURITY_GROUP_ID = 'sg-084dfa143cc85a5cf', INSTANCE_ID = 'i-04091b10d2cdc86aa'):
            '''
            detach, sgid, iid = sisa.split('/')
            ec2.detach_security_group_to_instance(sgid, iid)
        elif sisa.startswith('ssh'):
            '''
            create security group yg bs ssh utk vpcid
            /aws)ec2/sg/ssh/+/vpcid
            '''
            ssh, func, args = sisa.split('/')
            if func == '+':
                vpcid =args
                ec2.create_security_group_ssh(vpcid)

    elif jenis == 'subnet': # subnets
        if sisa.startswith('list'):
            if sisa == 'list':
                '''
                /aws)ec2/sn/list
                '''
                ec2.describe_subnets()
            else:
                '''
                /aws)ec2/subnet/list/vpcid
                '''
                vpcid = sisa.removeprefix('list/')
                ec2.describe_subnets(vpcid)
    elif jenis == 'ip': # allocated ip
        if sisa == 'list': # /aws)ec2/ip/list
            ec2.list_ip_addresses()


def handle_cf(request):
    if request == 'list':
        # /aws)ec2/list
        print('[cloudia] cf/list...')
        instances = cf.list_stacks()
        # pp(instances)
        # ebs.describe_environments()
        return
    elif request == 'list2':
        # /aws)ec2/list
        print('[cloudia] cf/list2 = describe stacks...')
        instances = cf.describe_stacks()
        # pp(instances)
        # ebs.describe_environments()
        return


def handle_kafka(request):
    """
    /aws)kafka/list
    /aws)kafka/detail/clusterarn
    /aws)kafka/delete/clusterarn
    /aws)kafka/+/name=...,subnets=sn1|sn2,sg=sg1|sg2,num=1
    """
    if request == 'list':
        # /aws)ec2/list
        print('[cloudia] kafka/list...')
        response = kafka.list_cluster()
        return
    if '/' in request:
        jenis, sisa = request.split('/', 1)
    else:
        jenis = request
        sisa = ''
    if jenis == 'detail':
        clusterarn = sisa
        response = kafka.describe_cluster(clusterarn)
    elif jenis == 'delete':
        clusterarn = sisa
        response = kafka.delete_cluster(clusterarn)
    elif jenis == '-':
        clusterarn = sisa
        response = kafka.delete_cluster(clusterarn)
    elif jenis == 'public':
        clusterarn = sisa
        response = kafka.make_public(clusterarn)
    elif jenis == 'status':
        clusterarn = sisa
        response = kafka.status(clusterarn)
    elif jenis == 'auth':
        clusterarn = sisa
        response = kafka.add_authentication(clusterarn)
    elif jenis == '+':
        items = sisa.split(',')
        kwargs = {}
        for item in items:
            k,v = item.split('=')
            if k == 'name':
                kwargs.update({
                    'cluster_name': v,
                })
            elif k == 'subnets':
                subnetlist = v.split('|')
                kwargs.update({
                    'subnet_list': subnetlist,
                })
            elif k == 'sg':
                secgroup_list = v.split('|')
                kwargs.update({
                    'subnet_list': secgroup_list,
                })
            elif k == 'num': # instances max count
                kwargs.update({
                    'jumlah_broker_per_subnet': int(v),
                })
        response = kafka.create_cluster(**kwargs)


def cloudia(request):

    if request == 'regions':
        '''
        /aws)regions
        '''
        regions = iam._factory.regions()
        print('[cloudia] peroleh regions:', regions)

    elif request .startswith('images'):
        '''
        /aws)images     = all (lama)
        /aws)images*    = self
            {'Images': [], 'ResponseMetadata': {'RequestId': 'd3d6591d-9373-42b3-94f0-f95b7e473cc6', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'd3d6591d-9373-42b3-94f0-f95b7e473cc6', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '219', 'date': 'Thu, 05 May 2022 22:44:13 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
        '''
        images = []
        if request == 'images':
            images = ec2.images()
        elif request == 'images*':
            images = ec2.images(True)
        print(images)

    elif request.startswith('iam'):
        '''
        /aws)iam/roles/rl
        /aws)iam/users/rl
        /aws)iam/users/rd/0
        /aws)iam/policies/rl
        /aws)iam/groups/rl
        /aws)iam/profiles/rl
        /aws)iam/accesskeys/rl/usef
        /aws)regions
        /aws)images
        '''
        print('[cloudia] iam function...')
        code = request.removeprefix('iam/')
        handle_iam(code)

    elif request.startswith('rds'):
        print('[cloudia] rds function...')
        code = request.removeprefix('rds/')
        handle_rds(code)

    elif request.startswith('vpc'):
        print('[cloudia] vpc function...')
        code = request.removeprefix('vpc/')
        handle_vpc(code)

    elif request.startswith('ebs'):
        print('[cloudia] ebs function...')
        code = request.removeprefix('ebs/')
        handle_ebs(code)

    elif request.startswith('ec2'):
        print('[cloudia] ec2 function...')
        code = request.removeprefix('ec2/')
        handle_ec2(code)

    elif request.startswith('lambda'):
        print('[cloudia] lambda function...')
        code = request.removeprefix('lambda/')
        handle_lambda(code)

    elif request.startswith('cf'):
        print('[cloudia] cloud formation function...')
        code = request.removeprefix('cf/')
        handle_cf(code)

    elif request.startswith('kafka'):
        print('[cloudia] kafka function...')
        code = request.removeprefix('kafka/')
        handle_kafka(code)

    elif request.startswith('subnet'):
        print('[cloudia] subnet function...')
        code = request.removeprefix('subnet/')
        handle_subnet(code)
