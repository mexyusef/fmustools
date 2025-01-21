--% index/fmus
.,d
	MyNoti.js,f(e=__FILE__=MyNoti.js)
	MyModal.js,f(e=__FILE__=MyModal.js)
--#

--% MyNoti.js
import React from "react";
// react plugin for creating notifications over the dashboard
import NotificationAlert from "react-notification-alert";
// react-bootstrap components
import {
	Alert,
	Badge,
	Button,
	Card,
	Modal,
	Navbar,
	Nav,
	Container,
	Row,
	Col,
} from "react-bootstrap";

// function MyNoti({showModal, setShowModal}) {
const MyNoti = React.forwardRef((props, ref) => {
	const notificationAlertRef = React.useRef(null);

  React.useImperativeHandle(
    ref,
    () => ({
      // place = tl, tc, tr, bl, bc, br
      // type = primary, success, danger, warning, info    
      notify(place='tr', type='primary') {
        var options = {};
        options = {
          place: place,
          message: (
            <div>
              <div>
                Welcome to <b>Fulgent Light</b> - a beautiful freebie for every web developer.
              </div>
            </div>
          ),
          type: type,
          icon: "nc-icon nc-bell-55",
          autoDismiss: 7,
        };
        notificationAlertRef.current.notificationAlert(options);
      },
    })
  );

  return (
    <>
      <div className="rna-container">
        <NotificationAlert ref={notificationAlertRef} />
      </div>
    </>
  );
});

export default MyNoti;
--#

--% MyModal.js
import React from "react";
// react plugin for creating notifications over the dashboard
import NotificationAlert from "react-notification-alert";
// react-bootstrap components
import {
	Alert,
	Badge,
	Button,
	Card,
	Modal,
	Navbar,
	Nav,
	Container,
	Row,
	Col,
} from "react-bootstrap";

function MyModal({showModal, setShowModal, tulisan='<p>Always have an access to your profile</p>'}) {
	// const [showModal, setShowModal] = React.useState(false);

  return (
  <>
    <Modal
      className="modal-mini modal-primary"
      show={showModal}
      onHide={() => setShowModal(false)}
      >

      <Modal.Header className="justify-content-center">
        <div className="modal-profile">
          <i className="nc-icon nc-bulb-63"></i>
        </div>
      </Modal.Header>

      <Modal.Body className="text-center">
        {tulisan}
      </Modal.Body>

      <div className="modal-footer">
        <Button
          className="btn-simple"
          type="button"
          variant="link"
          onClick={() => setShowModal(false)}
        >
          Back
        </Button>
        <Button
          className="btn-simple"
          type="button"
          variant="link"
          onClick={() => setShowModal(false)}
        >
          Close
        </Button>
      </div>
      
    </Modal>
  </>
  );
}
  
export default MyModal;
--#
