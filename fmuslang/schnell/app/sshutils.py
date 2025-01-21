# https://www.maskaravivek.com/post/how-to-ssh-into-an-ec2-instance-using-boto3/

"""
https://hackersandslackers.com/automate-ssh-scp-python-paramiko/
generate rsa keys
$ ssh-keygen -t rsa

copy key to remote
$ ssh-copy-id -i ~/.ssh/mykey username@my_remote_host.org

$ pip3 install paramiko scp
"""
import paramiko, time
from pyngrok import ngrok, conf

def ssh_connect_with_retry(ssh, ip_address, privkey, retries):
    if retries > 3:
        return False
    interval = 5
    try:
        retries += 1
        print('[sshutils] SSH into the instance: {}'.format(ip_address))
        ssh.connect(hostname=ip_address, username='ubuntu', pkey=privkey)
        return True
    except Exception as e:
        print(e)
        time.sleep(interval)
        print('[sshutils] Retrying SSH connection to {}'.format(ip_address))
        ssh_connect_with_retry(ssh, ip_address, retries)


def exec_ssh_connect_with_retry(ip_address, commands='ls -al'.encode('utf8'), privkey_pemfile='./config/image_rec_auth.pem', retries=0):
    print('[sshutils] exec_ssh_connect_with_retry started...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privkey = paramiko.RSAKey.from_private_key_file(privkey_pemfile)
    ssh_connect_with_retry(ssh, ip_address, privkey, retries)
    stdin, stdout, stderr = ssh.exec_command(commands)
    print('stdout:', stdout.read().decode('utf8'))
    print('stderr:', stderr.read().decode('utf8'))


def create_keypair_pem_file(keypair_name = "python_keypair.pem"):
    """
    https://stackoverflow.com/questions/32233873/create-new-ec2-keypair-on-aws-with-boto3
    https://stackoverflow.com/questions/10569653/boto-get-all-keypairs-method-and-the-save-of-its-results?noredirect=1&lq=1
    """
    import boto3
    from .fileutils import chmod
    ec2 = boto3.client('ec2')
    response = ec2.create_key_pair(KeyName=keypair_name)
    # private_key_file=open(keypair_name,"w")
    # private_key_file.write(response['KeyMaterial'])
    # private_key_file.close
    with open(keypair_name, 'w') as fd:
        print(f"[sshutils] writing response['KeyMaterial'] = {response['KeyMaterial']} to {keypair_name}")
        fd.write(response['KeyMaterial'])
    chmod(keypair_name, '400')


def set_tunnel_callback(callback):
    """
    def callback(log):
        print(str(log))
    """
    conf.get_default().log_event_callback = callback


def create_tunnel(port=80, protocol='tcp', log_callback=None):
    if log_callback:
        conf.get_default().log_event_callback = log_callback
    tunnel = ngrok.connect(port, protocol)
    print('[sshutils][create_tunnel]', tunnel)
    return tunnel


def create_tunnel_blocking(port=80, protocol='tcp', log_callback=None):
    """
    get_ngrok_process() mestinya terima port dan protocol

    The NgrokProcess contains an api_url variable, 
    usually initialized to http://127.0.0.1:4040, 
    from which we can access the ngrok client API.
    """
    if log_callback:
        conf.get_default().log_event_callback = log_callback
    ngrok_process = ngrok.get_ngrok_process()
    try:
        print('[sshutils][create_tunnel_blocking]', ngrok_process)
        # Block until CTRL-C or some other terminating event
        ngrok_process.proc.wait()
    except KeyboardInterrupt:
        print("[create_tunnel_blocking] Shutting down server.")
        ngrok.kill()


def list_tunnels():
    tunnels = ngrok.get_tunnels()
    print('[sshutils][list_tunnels]', tunnels)
    return tunnels


def close_tunnel(tunnel):
    ngrok.disconnect(tunnel.public_url)


def stop_monitoring():
    ngrok.get_ngrok_process().stop_monitor_thread()


