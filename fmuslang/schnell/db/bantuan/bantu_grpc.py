from schnell.app.printutils import (
  indah3
)

"""
syntax = "proto3";

service SensorService {
  rpc send_humidity(HumidityRequest) returns (HumidityResponse) {}
}

message HumidityRequest {
  string bysensor_building_id = 1;
  string bysensor_sensor_id = 2;
  string type = 3;
  string timestamp = 4;
  float value = 5;
}

message HumidityResponse {
  string ack = 1;
}
"""

from .common import TAB

field_map = {
  'string'            : 'string',
  'float'             : 'float',
  # int32, bytes
}

class GrpcOutput:
  def __init__(self, RootNode):
    # self.output = ''
    self.root = RootNode
    # self.service = RootNode.label
    self.tables = []
    self.tablenames = []
    self.service = []
    self._tables()
    self._service()


  def generate(self):
    header = '\n'.join(self.service)
    footer = '\n'.join(self.tables)
    return header + '\n' + footer


  def _service(self):
    self.service.append('\nsyntax = "proto3";')
    self.service.append(f'\nservice {self.root.dbname} {{')
    # rpc send_humidity(HumidityRequest) returns (HumidityResponse) {}
    # rpc send_humidity(HumidityRequest) {}
    # services = []
    for table in self.tablenames:
      svc = TAB+f"rpc send_{table.lower()}({table}) {{}}"
      self.service.append(svc)

    self.service.append('}')


  def _tables(self):
    for index, table in enumerate(self.root.children, 1):
      table_fields = []
      self.tablenames.append(table.model)
      for field_no, field in enumerate(table.children, 1):
        column = f"{field_map.get(field.type, field.type)} {field.label} = {field_no};"
        table_fields.append(column)
      
      stringified_fields = '\n'.join([TAB+item for item in table_fields])
      table = f"\nmessage {table.model} {{\n{stringified_fields}\n}}"
      self.tables.append(table)


def bantu_grpc(RootNode):
  indah3('bantu_grpc', warna='white')
  grpc = GrpcOutput(RootNode)
  return grpc.generate()
