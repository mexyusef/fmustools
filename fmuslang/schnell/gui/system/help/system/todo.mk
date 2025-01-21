--% contoh pertama dari django-react
ini kita lakukan begini saja...
kita bikin berbagai versi dari django, flask, fastapi, nodejs, nodets, nest, next,
berbagai java, dll

title,s; description,t; completed,b,df=false

kita lihat model dari django
```
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
```
sedangkan dari sisi react:

di sini kita buat input name: title, description, completed
```
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label
} from "reactstrap";
```

```
<Form>
    <FormGroup>
        <Label for="title">Title</Label>
        <Input
            type="text"
            name="title"
            value={this.state.activeItem.title}
            onChange={this.handleChange}
            placeholder="Enter Todo Title"
        />
    </FormGroup>

    <FormGroup>
        <Label for="description">Description</Label>
        <Input
            type="text"
            name="description"
            value={this.state.activeItem.description}
            onChange={this.handleChange}
            placeholder="Enter Todo description"
        />
    </FormGroup>

    <FormGroup check>
        <Label for="completed">
        <Input
            type="checkbox"
            name="completed"
            checked={this.state.activeItem.completed}
            onChange={this.handleChange}
            />
            Completed
        </Label>
    </FormGroup>
</Form>
```
--#
