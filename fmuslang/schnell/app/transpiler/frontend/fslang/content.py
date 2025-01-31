from app.fileutils import (
  file_copy,
  replace_entry,
  get_definition_by_key_permissive_start,
  replace_string_in_entry,
)
from .common import program_config, disini

def process_content():
  template = program_config['fe']
  filepath = joiner(disini, f'{template}/dashboard.mk')
  baris = '/react-light/src/views/Dashboard.js'
  content = get_definition_by_key_permissive_start(filepath, baris)
  if content:
    frontend_config['content'] = content



card_statistics = """
<Card className="card-stats">
  <Card.Body>
    <Row>
      <Col xs="5">
        <div className="icon-big text-center icon-warning">
          <i className="nc-icon nc-chart text-warning"></i>
        </div>
      </Col>
      <Col xs="7">
        <div className="numbers">
          <p className="card-category">Number</p>
          <Card.Title as="h4">150GB</Card.Title>
        </div>
      </Col>
    </Row>
  </Card.Body>
  <Card.Footer>
    <hr></hr>
    <div className="stats">
      <i className="fas fa-redo mr-1"></i>
      Update Now
    </div>
  </Card.Footer>
</Card>
"""
card_linechart = """
<Card>
  <Card.Header>
    <Card.Title as="h4">Users Behavior</Card.Title>
    <p className="card-category">24 Hours performance</p>
  </Card.Header>
  <Card.Body>
    <div className="ct-chart" id="chartHours">
      <ChartistGraph
        data={{
          labels: [
            "9:00AM",
            "12:00AM",
            "3:00PM",
            "6:00PM",
            "9:00PM",
            "12:00PM",
            "3:00AM",
            "6:00AM",
          ],
          series: [
            [287, 385, 490, 492, 554, 586, 698, 695],
            [67, 152, 143, 240, 287, 335, 435, 437],
            [23, 113, 67, 108, 190, 239, 307, 308],
          ],
        }}
        type="Line"
        options={{
          low: 0,
          high: 800,
          showArea: false,
          height: "245px",
          axisX: {
            showGrid: false,
          },
          lineSmooth: true,
          showLine: true,
          showPoint: true,
          fullWidth: true,
          chartPadding: {
            right: 50,
          },
        }}
        responsiveOptions={[
          [
            "screen and (max-width: 640px)",
            {
              axisX: {
                labelInterpolationFnc: function (value) {
                  return value[0];
                },
              },
            },
          ],
        ]}
      />
    </div>
  </Card.Body>
  <Card.Footer>
    <div className="legend">
      <i className="fas fa-circle text-info"></i>
      Open <i className="fas fa-circle text-danger"></i>
      Click <i className="fas fa-circle text-warning"></i>
      Click Second Time
    </div>
    <hr></hr>
    <div className="stats">
      <i className="fas fa-history"></i>
      Updated 3 minutes ago
    </div>
  </Card.Footer>
</Card>
"""
card_piechart = """
<Card>
  <Card.Header>
    <Card.Title as="h4">Email Statistics</Card.Title>
    <p className="card-category">Last Campaign Performance</p>
  </Card.Header>
  <Card.Body>
    <div
      className="ct-chart ct-perfect-fourth"
      id="chartPreferences"
    >
      <ChartistGraph
        data={{
          labels: ["40%", "20%", "40%"],
          series: [40, 20, 40],
        }}
        type="Pie"
      />
    </div>
    <div className="legend">
      <i className="fas fa-circle text-info"></i>
      Open <i className="fas fa-circle text-danger"></i>
      Bounce <i className="fas fa-circle text-warning"></i>
      Unsubscribe
    </div>
    <hr></hr>
    <div className="stats">
      <i className="far fa-clock"></i>
      Campaign sent 2 days ago
    </div>
  </Card.Body>
</Card>
"""
card_barchart = """
<Card>
  <Card.Header>
    <Card.Title as="h4">2017 Sales</Card.Title>
    <p className="card-category">All products including Taxes</p>
  </Card.Header>
  <Card.Body>
    <div className="ct-chart" id="chartActivity">
      <ChartistGraph
        data={{
          labels: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "Mai",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
          ],
          series: [
            [
              542,
              443,
              320,
              780,
              553,
              453,
              326,
              434,
              568,
              610,
              756,
              895,
            ],
            [
              412,
              243,
              280,
              580,
              453,
              353,
              300,
              364,
              368,
              410,
              636,
              695,
            ],
          ],
        }}
        type="Bar"
        options={{
          seriesBarDistance: 10,
          axisX: {
            showGrid: false,
          },
          height: "245px",
        }}
        responsiveOptions={[
          [
            "screen and (max-width: 640px)",
            {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc: function (value) {
                  return value[0];
                },
              },
            },
          ],
        ]}
      />
    </div>
  </Card.Body>
  <Card.Footer>
    <div className="legend">
      <i className="fas fa-circle text-info"></i>
      Tesla Model S <i className="fas fa-circle text-danger"></i>
      BMW 5 Series
    </div>
    <hr></hr>
    <div className="stats">
      <i className="fas fa-check"></i>
      Data information certified
    </div>
  </Card.Footer>
</Card>
"""

card_todo = """
<Card className="card-tasks">
  <Card.Header>
    <Card.Title as="h4">Tasks</Card.Title>
    <p className="card-category">Backend development</p>
  </Card.Header>
  <Card.Body>
    <div className="table-full-width">
      <Table>
        <tbody>
          <tr>
            <td>
              <Form.Check className="mb-1 pl-0">
                <Form.Check.Label>
                  <Form.Check.Input
                    defaultValue=""
                    type="checkbox"
                  ></Form.Check.Input>
                  <span className="form-check-sign"></span>
                </Form.Check.Label>
              </Form.Check>
            </td>
            <td>
              Sign contract for "What are conference organizers
              afraid of?"
            </td>
            <td className="td-actions text-right">
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-488980961">
                    Edit Task..
                  </Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="info"
                >
                  <i className="fas fa-edit"></i>
                </Button>
              </OverlayTrigger>
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-506045838">Remove..</Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="danger"
                >
                  <i className="fas fa-times"></i>
                </Button>
              </OverlayTrigger>
            </td>
          </tr>
          <tr>
            <td>
              <Form.Check className="mb-1 pl-0">
                <Form.Check.Label>
                  <Form.Check.Input
                    defaultChecked
                    defaultValue=""
                    type="checkbox"
                  ></Form.Check.Input>
                  <span className="form-check-sign"></span>
                </Form.Check.Label>
              </Form.Check>
            </td>
            <td>
              Lines From Great Russian Literature? Or E-mails From
              My Boss?
            </td>
            <td className="td-actions text-right">
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-537440761">
                    Edit Task..
                  </Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="info"
                >
                  <i className="fas fa-edit"></i>
                </Button>
              </OverlayTrigger>
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-21130535">Remove..</Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="danger"
                >
                  <i className="fas fa-times"></i>
                </Button>
              </OverlayTrigger>
            </td>
          </tr>
          <tr>
            <td>
              <Form.Check className="mb-1 pl-0">
                <Form.Check.Label>
                  <Form.Check.Input
                    defaultChecked
                    defaultValue=""
                    type="checkbox"
                  ></Form.Check.Input>
                  <span className="form-check-sign"></span>
                </Form.Check.Label>
              </Form.Check>
            </td>
            <td>
              Flooded: One year later, assessing what was lost and
              what was found when a ravaging rain swept through
              metro Detroit
            </td>
            <td className="td-actions text-right">
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-577232198">
                    Edit Task..
                  </Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="info"
                >
                  <i className="fas fa-edit"></i>
                </Button>
              </OverlayTrigger>
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-773861645">Remove..</Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="danger"
                >
                  <i className="fas fa-times"></i>
                </Button>
              </OverlayTrigger>
            </td>
          </tr>
          <tr>
            <td>
              <Form.Check className="mb-1 pl-0">
                <Form.Check.Label>
                  <Form.Check.Input
                    defaultChecked
                    type="checkbox"
                  ></Form.Check.Input>
                  <span className="form-check-sign"></span>
                </Form.Check.Label>
              </Form.Check>
            </td>
            <td>
              Create 4 Invisible User Experiences you Never Knew
              About
            </td>
            <td className="td-actions text-right">
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-422471719">
                    Edit Task..
                  </Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="info"
                >
                  <i className="fas fa-edit"></i>
                </Button>
              </OverlayTrigger>
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-829164576">Remove..</Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="danger"
                >
                  <i className="fas fa-times"></i>
                </Button>
              </OverlayTrigger>
            </td>
          </tr>
          <tr>
            <td>
              <Form.Check className="mb-1 pl-0">
                <Form.Check.Label>
                  <Form.Check.Input
                    defaultValue=""
                    type="checkbox"
                  ></Form.Check.Input>
                  <span className="form-check-sign"></span>
                </Form.Check.Label>
              </Form.Check>
            </td>
            <td>Read "Following makes Medium better"</td>
            <td className="td-actions text-right">
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-160575228">
                    Edit Task..
                  </Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="info"
                >
                  <i className="fas fa-edit"></i>
                </Button>
              </OverlayTrigger>
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-922981635">Remove..</Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="danger"
                >
                  <i className="fas fa-times"></i>
                </Button>
              </OverlayTrigger>
            </td>
          </tr>
          <tr>
            <td>
              <Form.Check className="mb-1 pl-0">
                <Form.Check.Label>
                  <Form.Check.Input
                    defaultValue=""
                    disabled
                    type="checkbox"
                  ></Form.Check.Input>
                  <span className="form-check-sign"></span>
                </Form.Check.Label>
              </Form.Check>
            </td>
            <td>Unfollow 5 enemies from twitter</td>
            <td className="td-actions text-right">
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-938342127">
                    Edit Task..
                  </Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="info"
                >
                  <i className="fas fa-edit"></i>
                </Button>
              </OverlayTrigger>
              <OverlayTrigger
                overlay={
                  <Tooltip id="tooltip-119603706">Remove..</Tooltip>
                }
              >
                <Button
                  className="btn-simple btn-link p-1"
                  type="button"
                  variant="danger"
                >
                  <i className="fas fa-times"></i>
                </Button>
              </OverlayTrigger>
            </td>
          </tr>
        </tbody>
      </Table>
    </div>
  </Card.Body>
  <Card.Footer>
    <hr></hr>
    <div className="stats">
      <i className="now-ui-icons loader_refresh spin"></i>
      Updated 3 minutes ago
    </div>
  </Card.Footer>
</Card>
"""

def process_item(item):
  """
  card_statistics
  card_piechart
  card_linechart
  card_barchart
  """
  kembali = ''
  nama = item['name']
  if nama == 'stat':
    kembali += card_statistics
  elif nama == 'pie':
    kembali += card_piechart
  elif nama == 'line':
    kembali += card_linechart
  elif nama == 'bar':
    kembali += card_barchart
  elif nama == 'todo':
    kembali += card_todo
  else:
    kembali += f'<{nama} />'
  return kembali


def process_column(item):
  kolom = ''
  nama = item['name']
  if nama == 'col12':
    kolom += '<Col md="12">__TEMPLATE_ITEMS</Col>'
  elif nama == 'col10':
    kolom += '<Col md="10">__TEMPLATE_ITEMS</Col>'
  elif nama == 'col8':
    kolom += '<Col md="8">__TEMPLATE_ITEMS</Col>'
  elif nama == 'col6':
    kolom += '<Col md="6">__TEMPLATE_ITEMS</Col>'
  elif nama == 'col5':
    kolom += '<Col md="5">__TEMPLATE_ITEMS</Col>'
  elif nama == 'col4':
    kolom += '<Col md="4">__TEMPLATE_ITEMS</Col>'
  elif nama == 'col3':
    kolom += '<Col md="3">__TEMPLATE_ITEMS</Col>'
  elif nama == 'col2':
    kolom += '<Col md="2">__TEMPLATE_ITEMS</Col>'
  elif nama == 'col1':
    kolom += '<Col md="1">__TEMPLATE_ITEMS</Col>'
  if item['children']:
    barang = []
    for hitam in item['children']:
      # bentuk = f'<{hitam["name"]} />'
      bentuk = process_item(hitam)
      barang.append(bentuk)
    bentukan = '\n'.join(barang)
    kolom = kolom.replace('__TEMPLATE_ITEMS', bentukan)
  return kolom


def create_dashboard(items):
  kembali = '<Row>'
  # print('ketemu', items)
  for item in items:
    kembali += process_column(item)
  kembali += '</Row>'
  return kembali
