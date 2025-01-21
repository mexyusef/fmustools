--% index/fmus
            <Footer />
--#

--% /react-light/src/components/Footer/Footer.js
import React, { Component } from "react";
import { Container } from "react-bootstrap";

class Footer extends Component {
	render() {
		return (
			<footer className="footer px-0 px-lg-3">
				<Container fluid>
					<nav>

__TEMPLATE_FOOTER_ITEMS

					</nav>
				</Container>
			</footer>
		);
	}
}

export default Footer;
--#
