package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;


@Service
public class __TEMPLATE_TABLENAME_CASE__Service {

  @Autowired
  private __TEMPLATE_TABLENAME_CASE__Repository __TEMPLATE_TABLENAME_LOWER__Repository;

  public List<__TEMPLATE_TABLENAME_CASE__> findAll() {
    return __TEMPLATE_TABLENAME_LOWER__Repository.findAll();
  }

  public __TEMPLATE_TABLENAME_CASE__ findById(Long id) {
    return __TEMPLATE_TABLENAME_LOWER__Repository.findById(id).orElse(null);
  }

  public List<__TEMPLATE_TABLENAME_CASE__> findByName(String name) {
    // return __TEMPLATE_TABLENAME_LOWER__Repository.findByName(name);
    return __TEMPLATE_TABLENAME_LOWER__Repository.findByNameIgnoreCaseContaining(name);
  }

  public __TEMPLATE_TABLENAME_CASE__ save(__TEMPLATE_TABLENAME_CASE__ __TEMPLATE_TABLENAME_LOWER__) {
    return __TEMPLATE_TABLENAME_LOWER__Repository.save(__TEMPLATE_TABLENAME_LOWER__);
  }

  public void delete(Long id) {
    __TEMPLATE_TABLENAME_LOWER__Repository.deleteById(id);
  }

}