def react_bootstrap_form1(names, jenis, attrs):
  """
  helper utk transform_columns utk UI
  """


form_item_image = """<Form.Group controlId='__COLUMN_LOWER__'>
  <Form.Label>__COLUMN_ASIS__</Form.Label>
  <Form.Control
    type='text'
    placeholder='Enter __COLUMN_LOWER__'
    value={__COLUMN_ASIS__}
    onChange={(e) => set__COLUMN_UPFIRST__(e.target.value)}
  >
  </Form.Control>

    <Form.File
      id='image-file'
      label='Choose File'
      custom
      onChange={uploadFileHandler}
    >
    </Form.File>
    {uploading && <Loader />}

</Form.Group>"""

def get_form_item_image(column_name):
  return form_item_image.replace('__COLUMN_TITLE__', column_name).replace('__COLUMN_LOWER__', column_name.lower())

form_item_string = """<Form.Group controlId='__COLUMN_LOWER__'>
  <Form.Label>__COLUMN_ASIS__</Form.Label>
  <Form.Control
    type='text'
    placeholder='Enter __COLUMN_LOWER__'
    value={__COLUMN_ASIS__}
    onChange={(e) => set__COLUMN_UPFIRST__(e.target.value)}
  >
  </Form.Control>
</Form.Group>"""

def get_form_item_string(column_name):
  return form_item_string.replace('__COLUMN_TITLE__', column_name).replace('__COLUMN_LOWER__', column_name.lower())


form_item_integer = """<Form.Group controlId='__COLUMN_LOWER__'>
  <Form.Label>__COLUMN_ASIS__</Form.Label>
  <Form.Control
    type='number'
    placeholder='Enter __COLUMN_LOWER__'
    value={__COLUMN_ASIS__}
    onChange={(e) => set__COLUMN_UPFIRST__(e.target.value)}
  >
  </Form.Control>
</Form.Group>"""

def get_form_item_integer(column_name):
  return form_item_integer.replace('__COLUMN_TITLE__', column_name).replace('__COLUMN_LOWER__', column_name.lower())

form_item_selection = """<Form.Group controlId='rating'>
  <Form.Label>Rating</Form.Label>
  <Form.Control
    as='select'
    value={rating}
    onChange={(e) => setRating(e.target.value)}
  >
    <option value=''>Select...</option>
    <option value='1'>1 - Poor</option>
    <option value='2'>2 - Fair</option>
    <option value='3'>3 - Good</option>
    <option value='4'>4 - Very Good</option>
    <option value='5'>5 - Excellent</option>
  </Form.Control>
</Form.Group>"""

listgroup_item_selection = """
<ListGroup.Item>
  <Row>
    <Col>Qty</Col>
    <Col xs='auto' className='my-1'>
      <Form.Control
        as="select"
        value={qty}
        onChange={(e) => setQty(e.target.value)}
      >
        {
          [...Array(product.countInStock).keys()].map((x) => (
            <option key={x + 1} value={x + 1}>
              {x + 1}
            </option>
          ))
        }
      </Form.Control>
    </Col>
  </Row>
</ListGroup.Item>
"""

form_item_textarea = """<Form.Group controlId='comment'>
  <Form.Label>Review</Form.Label>
  <Form.Control
    as='textarea'
    row='5'
    value={comment}
    onChange={(e) => setComment(e.target.value)}
  ></Form.Control>
</Form.Group>"""

form_skeleton = """
<Form onSubmit={submitHandler}>
  <Button
    disabled={loadingProductReview}
    type='submit'
    variant='primary'
  >
    Submit
  </Button>

</Form>
"""