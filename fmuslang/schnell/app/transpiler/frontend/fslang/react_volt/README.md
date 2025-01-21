mari oprek header dulu
F<<layout(footer(copy,home,company,product,blog))>>

F<<layout(content(row(col6(item1),col6(item2)), row(col12(item3)) ))>>
F<<layout(content(row(col6(pie),col6(line)), row(col12(stat)) ))>>

F<<layout(header(left(title),right(search,drop1,drop2,account,logout)))>>
*/F<<layout(header(left(title),right(search,drop1,drop2,account,logout)))>>
F<<layout(sidebar(menu(section1(group1(item1,item2)),section2(group5(item5,item6)))))>>
*/F<<layout(sidebar(menu(section1(group1(item1,item2)),section2(group5(item5,item6)))))>>
F<<layout(sidebar(menu(user(cart(create,list), profile(create,list)),admin(category(create,list), product(create,list)))))>>

F<<layout(footer(copy,home,company,product,blog),content(row(col6(pie),col6(line)), row(col12(stat)) ),header(left(title),right(search,drop1,drop2,account,logout)),sidebar(menu(user(cart(create,list), profile(create,list)),admin(category(create,list), product(create,list)))))>>

F<<layout(footer(copy,home,company,product,blog),content(row(col6(pie),col6(line)), row(col2(stat),col10(todo)) ),header(left(title),right(search,drop1,drop2,account,logout)),sidebar(menu(user(cart(create,list), profile(create,list)),admin(category(create,list), product(create,list)))))>>

F<<
layout(
  footer(copy,home,company,product,blog),
  
  content(
    row(col6(pie),col6(line)), 
    row(col12(stat)) 
  ),
  
  header(
    left(title),
    right(search,drop1,drop2,account,logout)
  ),
  
  sidebar(menu(user(cart(create,list), profile(create,list)),admin(category(create,list), product(create,list))))
)
>>

if left:
          <Nav className="nav mr-auto" navbar>
          </Nav>
if right:
          <Nav className="ml-auto" navbar>
          </Nav>

header(
left(title),
right(search,drop1,drop2,account,logout),
)

__TEMPLATE_NAV_ITEMS

F<<layout(sidebar(menu(section1(group1(item1,item2)),section2(group5(item5,item6)))))>>
*/F<<layout(sidebar(menu(section1(group1(item1,item2)),section2(group5(item5,item6)))))>>

kita perkenalkan istilah
menu section      user, admin
  menu group      cart, profile, category, product
    menu item     create, list
--
sidebar(
  menu(
    user(cart(create,list), profile(create,list))
    ,
    admin(category(create,list), product(create,list))
  )
)

F<<layout(sidebar(menu(user(cart(create,list), profile(create,list)),admin(category(create,list), product(create,list)))))>>
*/F<<layout(sidebar(menu(user(cart(create,list), profile(create,list)),admin(category(create,list), product(create,list)))))>>
__TEMPLATE_MENU_CALL
__TEMPLATE_MENU_DECLARE

            <SidebarBottom judul='Menu 1' data={Menu1}/>
            <hr className="my-4 md:min-w-full" />
            <SidebarBottom judul='Menu 2' data={Menu2}/>
            <hr className="my-4 md:min-w-full" />
            <SidebarBottom judul='Menu 3' data={Menu3}/>

const Menu1 = [
  {
    title: 'Section 1',
    path: '#',
    icon: <AiIcons.AiFillHome />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,

    subNav: [
      {
        title: 'Dashboard',
        path: '/admin/dashboard',
        icon: <IoIcons.IoIosPaper />
      },
      {
        title: 'User Profile',
        path: '/admin/user',
        icon: <IoIcons.IoIosPaper />
      },
    ]
  },
]

const section1 = [
  {
    title:"group1", 
    path:"group1", 
    subNav: [
      { title:"item1", path:"item1" }, 
      { title:"item2", path:"item2" }
    ]
  }
]
==
        <Navbar.Collapse id="basic-navbar-nav">

          <Nav className="nav mr-auto" navbar>
          </Nav>

          <Nav className="ml-auto" navbar>
          </Nav>

        </Navbar.Collapse>
search bar
            <Nav.Item>
              <Nav.Link
                className="m-0"
                href="#pablo"
                onClick={(e) => e.preventDefault()}
              >
                <i className="nc-icon nc-zoom-split"></i>
                <span className="d-lg-block"> Search</span>
              </Nav.Link>
            </Nav.Item>

title
            <Nav.Item>
              <Nav.Link
                data-toggle="dropdown"
                href="#pablo"
                onClick={(e) => e.preventDefault()}
                className="m-0"
              >
                <i className="nc-icon nc-palette"></i>
                <span className="d-lg-none ml-1">Dashboard</span>
              </Nav.Link>
            </Nav.Item>

account
            <Nav.Item>
              <Nav.Link
                className="m-0"
                href="#pablo"
                onClick={(e) => e.preventDefault()}
              >
                <span className="no-icon">Account</span>
              </Nav.Link>
            </Nav.Item>

logout
            <Nav.Item>
              <Nav.Link
                className="m-0"
                href="#pablo"
                onClick={(e) => e.preventDefault()}
              >
                <span className="no-icon">Log out</span>
              </Nav.Link>
            </Nav.Item>

dropdown badge

            <Dropdown as={Nav.Item}>
              <Dropdown.Toggle
                as={Nav.Link}
                data-toggle="dropdown"
                id="dropdown-67443507"
                variant="default"
                className="m-0"
              >
                <i className="nc-icon nc-planet"></i>
                <span className="notification">5</span>
                <span className="d-lg-none ml-1">Notification</span>
              </Dropdown.Toggle>

              <Dropdown.Menu>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Notification 1
                </Dropdown.Item>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Notification 2
                </Dropdown.Item>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Notification 3
                </Dropdown.Item>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Notification 4
                </Dropdown.Item>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Another notification
                </Dropdown.Item>
              </Dropdown.Menu>

            </Dropdown>

drop down #2
            <Dropdown as={Nav.Item}>
              <Dropdown.Toggle
                aria-expanded={false}
                aria-haspopup={true}
                as={Nav.Link}
                data-toggle="dropdown"
                id="navbarDropdownMenuLink"
                variant="default"
                className="m-0"
              >
                <span className="no-icon">Dropdown</span>
              </Dropdown.Toggle>

              <Dropdown.Menu aria-labelledby="navbarDropdownMenuLink">
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Action
                </Dropdown.Item>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Another action
                </Dropdown.Item>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Something
                </Dropdown.Item>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Something else here
                </Dropdown.Item>
                <div className="divider"></div>
                <Dropdown.Item
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                >
                  Separated link
                </Dropdown.Item>
              </Dropdown.Menu>

            </Dropdown>

footer copyright
            <p className="copyright text-center">
              © {new Date().getFullYear()}{" "}
              <a href="http://www.creative-tim.com">Creative Tim</a>, made with
              love for a better web
            </p>
footer link
              <li>
                <a href="#pablo" onClick={(e) => e.preventDefault()}>
                  Blog
                </a>
              </li>

component/view
content(
  row(
    12(comp)
  ),
  row(
    10(comp),2(comp)
  ),
  row(
    8(comp),4(comp)
  ),
  row(
    4(comp),8(comp)
  ),
  row(
    6(comp),6(comp)
  ),
  row(
    4(comp),4(comp),4(comp)
  ),
  row(
    3(comp),3(comp),3(comp),3(comp)
  ),
)

bandingkan
sidebar     content
menu        row
section     col12,10,8,6,4,3,2
group       
item

F<<layout(content(row(col6(item1),col6(item2)), row(col12(item3)) ))>>
F<<layout(content(row(col6(pie),col6(line)), row(col12(stat)) ))>>


{
    "name": "row",
    "children": [
        {
            "name": "col12",
            "children": [
                {
                    "name": "item3",
                    "children": "",
                    "config": ""
                }
            ],
            "config": ""
        }
    ],
    "config": ""
}
function TableList() {
  return (
    <>
      <Container fluid>

        <Row>
          <Col md="12">
          </Col>
          <Col md="12">
          </Col>
        </Row>

        <Row>
          <Col lg="3" sm="6">
          </Col>
          <Col lg="3" sm="6">
          </Col>
          <Col lg="3" sm="6">
          </Col>
          <Col lg="3" sm="6">
          </Col>
        </Row>

        <Row>
          <Col md="6">
          </Col>
          <Col md="6">
          </Col>
        </Row>

      </Container>
    </>
  );
}
mari bikin bahasa utk content/main
pada dasarnya card...
bisa statistik, chart: pie, line, bar
(juga nanti dukung table)

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

line chart users behavior
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
pie chart email statistics
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
bar chart 2017 sales
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

== footer
list part: 
						<ul className="footer-menu">
home
							<li>
								<a href="#pablo" onClick={(e) => e.preventDefault()}>
									Home
								</a>
							</li>
company
							<li>
								<a href="#pablo" onClick={(e) => e.preventDefault()}>
									Company
								</a>
							</li>
portfolio
							<li>
								<a href="#pablo" onClick={(e) => e.preventDefault()}>
									Portfolio
								</a>
							</li>
blog
							<li>
								<a href="#pablo" onClick={(e) => e.preventDefault()}>
									Blog
								</a>
							</li>
						</ul>
copyright
						<p className="copyright text-center">
							© {new Date().getFullYear()}{" "}
							<a href="http://fulgent.de">Fulgent</a>, made with love for a better web
						</p>
F<<layout(footer(copy,home,company,product,blog))>>

onClick={()=>pemberitahuan.current.notify('tc', 'primary')}
onClick={(e) => setShowModal(true)}

https://github.com/facebook/create-react-app/issues/9904
FAST_REFRESH=false
CHOKIDAR_USEPOLLING=true
