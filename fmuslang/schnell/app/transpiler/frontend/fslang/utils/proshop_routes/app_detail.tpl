import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Row, Col, Image, ListGroup, Button, Card, Form } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { __TABLENAME_LOWER__Detail } from '../../store/__TABLENAME_LOWER__/__TABLENAME_LOWER__Actions'

const __TABLENAME_CASE__Detail = ({ match, history }) => {

	const { __TABLENAME_LOWER__ } = useSelector(state => state.__TABLENAME_LOWER__Detail)
	const dispatch = useDispatch()

  useEffect(() => {
    dispatch(__TABLENAME_LOWER__Detail(match.params.id))
  }, [dispatch, match])

	return (<>
		<Link to='/' className='btn btn-light my-3'>Back</Link>
		<h1>__TABLENAME_CASE__Detail</h1>
		{/* <h4>{JSON.stringify(product)}</h4> */}
		<div>
			<Row>
				<Col md={12}>
					<ListGroup variant="flush">
						<ListGroup.Item>
							<h3>{__TABLENAME_LOWER__.__FIRST_FIELD__}</h3>
						</ListGroup.Item>
					</ListGroup>
				</Col>
			</Row>
		</div>
	</>);
};

export default __TABLENAME_CASE__Detail;