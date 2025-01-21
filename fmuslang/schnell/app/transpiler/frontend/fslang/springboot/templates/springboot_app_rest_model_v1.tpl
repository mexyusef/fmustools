package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__;

// import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;


@Entity
@Data
@Table(name = "__TEMPLATE_TABLENAME_LOWER__")
public class __TEMPLATE_TABLENAME_CASE__ {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  private String name;

}
