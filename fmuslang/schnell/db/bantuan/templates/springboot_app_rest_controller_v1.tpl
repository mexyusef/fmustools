package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__;

import java.util.List;

import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;


@AllArgsConstructor
@RestController
@RequestMapping("/__TEMPLATE_TABLENAME_LOWER__")
public class __TEMPLATE_TABLENAME_CASE__Controller {

  private __TEMPLATE_TABLENAME_CASE__Mapper __TEMPLATE_TABLENAME_LOWER__Mapper;

  // http://localhost:__TEMPLATE_SERVER_PORT__/__TEMPLATE_TABLENAME_LOWER__
  @GetMapping(produces = {MediaType.APPLICATION_JSON_VALUE})
  public List<__TEMPLATE_TABLENAME_CASE__> getAll() {
    return __TEMPLATE_TABLENAME_LOWER__Mapper.findAll();
  }

  // http://localhost:__TEMPLATE_SERVER_PORT__/__TEMPLATE_TABLENAME_LOWER__/3
  // @GetMapping(path="{id}", produces = {MediaType.APPLICATION_JSON_VALUE})
  @GetMapping("{id}")
  public __TEMPLATE_TABLENAME_CASE__ getById(@PathVariable("id") long id) {
    return __TEMPLATE_TABLENAME_LOWER__Mapper.findById(id);
  }

  // http://localhost:__TEMPLATE_SERVER_PORT__/__TEMPLATE_TABLENAME_LOWER__/name/gaia
  @GetMapping("/name/{name}")
  public __TEMPLATE_TABLENAME_CASE__ getById(@PathVariable("name") String name) {
    return __TEMPLATE_TABLENAME_LOWER__Mapper.findByName(name);
  }

  @PostMapping
  public List<__TEMPLATE_TABLENAME_CASE__> create__TEMPLATE_TABLENAME_CASE__(
    @RequestBody
    __TEMPLATE_TABLENAME_CASE__ __TEMPLATE_TABLENAME_LOWER__
  ) {
    __TEMPLATE_TABLENAME_LOWER__Mapper.insert(__TEMPLATE_TABLENAME_LOWER__);
    return __TEMPLATE_TABLENAME_LOWER__Mapper.findAll();
  }

  @PutMapping("{id}")
  public __TEMPLATE_TABLENAME_CASE__ delete(
    @PathVariable("id") long id,
    @RequestBody __TEMPLATE_TABLENAME_CASE__ __TEMPLATE_TABLENAME_LOWER__
  ) {
    __TEMPLATE_TABLENAME_LOWER__Mapper.update__TEMPLATE_TABLENAME_CASE__(id, __TEMPLATE_TABLENAME_LOWER__);
    return __TEMPLATE_TABLENAME_LOWER__Mapper.findById(id);
  }

  @DeleteMapping("{id}")
  public List<__TEMPLATE_TABLENAME_CASE__> delete(@PathVariable("id") long id) {
    __TEMPLATE_TABLENAME_LOWER__Mapper.delete(id);
    return __TEMPLATE_TABLENAME_LOWER__Mapper.findAll();
  }

}
