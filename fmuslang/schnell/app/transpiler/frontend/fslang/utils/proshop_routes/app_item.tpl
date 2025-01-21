import React from 'react'
import { Card } from 'react-bootstrap'
import { Link } from 'react-router-dom'

const __TABLENAME_CASE__Item = ({ __TABLENAME_LOWER__ }) => {
	return (<>
		<h1>__TABLENAME_CASE__Item</h1>
		<Card className="my-3 p-3 rounded">
      <Card.Body>
        <Link to={`/__TABLENAME_LOWER__/${__TABLENAME_LOWER__._id}`}>
          <Card.Title as="div">
            <strong>
						{__TABLENAME_LOWER__.__FIRST_FIELD__}
						</strong>
          </Card.Title>
        </Link>

        <Card.Text as="div">
          isi text #1
        </Card.Text>

        <Card.Text as="h3">
          isi text #2
        </Card.Text>
      </Card.Body>
		</Card>
	</>);
};

export default __TABLENAME_CASE__Item;
