# https://docs.docker.com/engine/api/sdk/examples/
# https://docker-py.readthedocs.io/en/stable/index.html
# https://docker-py.readthedocs.io/en/stable/containers.html
# https://docker-py.readthedocs.io/en/stable/images.html
# pip install docker
import docker

"""
TODO:
get all containers of one image
stop all containers of one image
remove all containers of one image
remove one image + remove all containers of one image

docker language

https://docker-py.readthedocs.io/en/stable/containers.html
client.containers
  run()
  create()
  get()
  list()
  prune()
container
  id
  image
  labels
  name
  short_id
  status
  attach()
  attach_socket()
  commit()
  diff()
  exec_run()
  export()
  get_archive()
  kill()
  logs()
  pause()
  put_archive()
  reload()
  remove()
  rename()
  resize()
  restart()
  start()
  stats()
  stop()
  top()
  unpause()
  update()
  wait()

https://docker-py.readthedocs.io/en/stable/images.html
client.images
  build()
  get()
  get_registry_data()
  list()
  load()
  prune()
  pull()
  push()
  remove()
  search()
image
  id
  labels
  short_id
  tags
  history()
  reload()
  save()
  tag()
"""

from .utils import (
  perintahsp_simple
)

is_dockering = False
docker_client = None


def get_client(cached=True):
  global docker_client, is_dockering
  if cached and docker_client is not None:
    return docker_client
  try:
    docker_client = docker.from_env()
    is_dockering = True
    return docker_client
  except Exception as err:
    print('docker.from_env():', err)
    return None


def run_container_background(container_name):
  if not is_dockering:
    print('not dockering')
    return
  container = docker_client.containers.run(container_name, detach=True)
  container.logs()


def run_image(container_image, command=None):
  if not is_dockering:
    print('not dockering')
    return
  args = {
    'image': container_image
  }
  if command:
    args.update({
      'command': command
    })
  docker_client.containers.run(**args)


def list_containers(all=False, list_callback=None, item_callback=None):
  containers = docker_client.containers.list(all=all)
  for container in containers:    
    if item_callback is not None:
      item_callback(container)
    else:
      print(f'cont id = {container.short_id}, name = {container.name}')

  if list_callback is not None:
    list_callback(containers)


def container_images(all=False):
  """
  list of container-image
  """
  containers = docker_client.containers.list(all=all)
  images = {}
  for container in containers:
    images[container] = container.attrs['Config']['Image']
  return images


def container_list_by_image(imagename, exact=True):
  containers = docker_client.containers.list()
  if exact:
    return [container for container in containers if container.attrs['Config']['Image'] == imagename]
  else:
    return [container for container in containers if imagename in container.attrs['Config']['Image']]


def stop_containers():
  for container in docker_client.containers.list():
    container.stop()


def get_container_log(container_shortid):
  container = docker_client.containers.get(container_shortid)
  print(container.logs())


def list_images():
  daftar = docker_client.images.list()
  # print('jenis', type(daftar))
  # balik = list(daftar).reverse()
  for image in daftar:
    # print(image.id)
    nilai = int(image.attrs['Size'])
    ukuran = '{:,.0f}'.format(nilai/float(1<<20))+" MB"
    identitas = image.short_id.removeprefix('sha256:')
    print(f'image id = {identitas}, tags = {image.tags}, size = {ukuran}')


def list_images_empty():
  kosong = [img for img in docker_client.images.list() if img.tags == []]
  # print('peroleh:', kosong)
  for image in kosong:
    nilai = int(image.attrs['Size'])
    ukuran = '{:,.0f}'.format(nilai/float(1<<20))+" MB"
    identitas = image.short_id.removeprefix('sha256:')
    print(f'image id = {identitas}, tags = {image.tags}, size = {ukuran}')
    yn = input(f'\thapus image id = {image.short_id}, tags = {image.tags}? ')
    if yn == 'y':
      docker_client.images.remove(image.short_id)


def remove_container(container_id):
  """
  dc9e694984b3  ini yg dari "docker" dan kita jadikan args
  dc9e694984    ini short id kita
  55fb18cc6b
  """
  print('removing', container_id, type(container_id))
  # bukan == tapi 'in' krn args dari user lebih panjang 2 chars
  image = [img for img in docker_client.containers.list(all=True) if img.short_id in container_id]
  if image and len(image)==1:
    container = image[0]
    yn = input(f'\thapus container id = {container.short_id}, name = {container.name}? ')
    if yn == 'y':
      container.remove()


def stop_container(container_id):
  print('stopping', container_id, type(container_id))
  image = [img for img in docker_client.containers.list() if img.short_id == container_id]
  if image and len(image)==1:
    container = image[0]
    yn = input(f'\tstop container id = {container.short_id}, name = {container.name}? ')
    if yn == 'y':
      container.stop()


def remove_image(image_id):
  print('removing', image_id, type(image_id))
  image = [img for img in docker_client.images.list() if img.short_id == 'sha256:'+image_id]
  if not image:
    image = [img for img in docker_client.images.list() if img.tags[0] == image_id]
  if image and len(image) > 1:
    from schnell.app.printutils import print_list_warna
    print('sempitkan pilihan untuk dihapus')
    images = []
    for img in image:
      nilai = int(img.attrs['Size'])
      ukuran = '{:,.0f}'.format(nilai/float(1<<20))+" MB"
      identitas = image.short_id.removeprefix('sha256:')
      data = f'image id = {identitas}, tags = {img.tags}, size = {ukuran}'
      images.append(data)
    print_list_warna(images)
    return
  if image:
    image = image[0]
    nilai = int(image.attrs['Size'])
    ukuran = '{:,.0f}'.format(nilai/float(1<<20))+" MB"
    identitas = image.short_id.removeprefix('sha256:')
    print(f'image id = {identitas}, tags = {image.tags}, size = {ukuran}')
    yn = input(f'\thapus image id = {image.short_id}, tags = {image.tags}? ')
    if yn == 'y':
      docker_client.images.remove(image.short_id)
  else:
    print('not found')


def pull_image(image_name, client=docker_client):
  image = client.images.pull(image_name)
  print(image.id)


def docker_start(container_name):
  perintahsp_simple(f'docker start {container_name}')
