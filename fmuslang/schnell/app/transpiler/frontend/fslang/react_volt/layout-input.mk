--% /react-light/src/layouts/Admin.js
import React, { Component } from "react";
import { useLocation, Route, Switch } from "react-router-dom";

import AdminNavbar from "components/Navbars/AdminNavbar";
import Footer from "components/Footer/Footer";
import Sidebar from "components/Sidebar/Sidebar";
import FixedPlugin from "components/FixedPlugin/FixedPlugin.js";

import routes from "routes.js";
import sidebarImage from "assets/img/sidebar-3.jpg";
import './Admin.css';

function Admin() {
	const [image, setImage] = React.useState(sidebarImage);
	const [color, setColor] = React.useState("black");
	const [hasImage, setHasImage] = React.useState(true);

	const location = useLocation();
	const mainPanel = React.useRef(null);
	const [openSidebar, setOpenSidebar] = React.useState(false);

	const getRoutes = (routes) => {
		return routes.map((prop, key) => {
			if (prop.layout === "/admin") {
				return (
					<Route
						path={prop.layout + prop.path}
						render={(props) => <prop.component {...props} />}
						key={key}
					/>
				);
			} else {
				return null;
			}
		});
	};

	React.useEffect(() => {
		// document.documentElement.scrollTop = 0;
		// document.scrollingElement.scrollTop = 0;
		// mainPanel.current.scrollTop = 0;
		// if (
		//   window.innerWidth < 993 &&
		//   document.documentElement.className.indexOf("nav-open") !== -1
		// ) {
		//   document.documentElement.classList.toggle("nav-open");
		//   var element = document.getElementById("bodyClick");
		//   element.parentNode.removeChild(element);
		// }
	}, [location]);

	return (
		<>
			<div>
				
        <Sidebar 
          active_classname={openSidebar ? 'sidebar-layout active' : 'sidebar-layout'}
          is_active={openSidebar}
          togglerMenu={()=>{
            setOpenSidebar(!openSidebar);
          }}
          color={color} 
          image={hasImage ? image : ""} 
          routes={routes} 
          />

				<main className={'content main-section' + (openSidebar?' active':'')}>
					<div className="main-panel" ref={mainPanel}>

						<AdminNavbar />

            <div className="content">
              <Switch>{getRoutes(routes)}</Switch>
            </div>

            <Footer />

					</div>
				</main>

			</div>

__TEMPLATE_RIGHTBAR

		</>
	);

}

export default Admin;
--#
