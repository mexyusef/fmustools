package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__;

// import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__.__TEMPLATE_TABLENAME_CASE__;
// import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__.__TEMPLATE_TABLENAME_CASE__Service;

import com.coxautodev.graphql.tools.GraphQLQueryResolver;

import java.util.List;

import lombok.RequiredArgsConstructor;


@RequiredArgsConstructor
public class __TEMPLATE_TABLENAME_CASE__Query implements GraphQLQueryResolver {

  //private final __TEMPLATE_TABLENAME_CASE__Service __TEMPLATE_TABLENAME_LOWER__Service;
  private __TEMPLATE_TABLENAME_CASE__Service __TEMPLATE_TABLENAME_LOWER__Service;
  
  public __TEMPLATE_TABLENAME_CASE__Query(__TEMPLATE_TABLENAME_CASE__Service __TEMPLATE_TABLENAME_LOWER__Service) {
    this.__TEMPLATE_TABLENAME_LOWER__Service = __TEMPLATE_TABLENAME_LOWER__Service;
  }

  public List<__TEMPLATE_TABLENAME_CASE__> find__TEMPLATE_TABLENAME_CASE__ByName(String name) {
    return __TEMPLATE_TABLENAME_LOWER__Service.findByName(name);
  }

  public __TEMPLATE_TABLENAME_CASE__ find__TEMPLATE_TABLENAME_CASE__ById(Long id) {
    return __TEMPLATE_TABLENAME_LOWER__Service.findById(id);
  }

  public List<__TEMPLATE_TABLENAME_CASE__> all__TEMPLATE_TABLENAME_CASE__s() {
    return __TEMPLATE_TABLENAME_LOWER__Service.findAll();
  }

}
