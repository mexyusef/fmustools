package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
// import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;

import org.springframework.stereotype.Repository;


@Mapper
@Repository
public interface __TEMPLATE_TABLENAME_CASE__Mapper {

  @Select("select * from __TEMPLATE_TABLENAME_LOWER__ where name = #{name}")
  __TEMPLATE_TABLENAME_CASE__ findByName(@Param("name") String name);

  @Select("select * from __TEMPLATE_TABLENAME_LOWER__ where id = #{id}")
  __TEMPLATE_TABLENAME_CASE__ findById(@Param("id") long id);
  
  List<__TEMPLATE_TABLENAME_CASE__> findAll();

  void insert(@Param("__TEMPLATE_TABLENAME_LOWER__") __TEMPLATE_TABLENAME_CASE__ __TEMPLATE_TABLENAME_LOWER__);

  // @Update("update __TEMPLATE_TABLENAME_LOWER__ set name=#{__TEMPLATE_TABLENAME_LOWER__.name},state=#{__TEMPLATE_TABLENAME_LOWER__.state},country=#{__TEMPLATE_TABLENAME_LOWER__.country} where id=#{id}")
  void update__TEMPLATE_TABLENAME_CASE__(@Param("id") long id, __TEMPLATE_TABLENAME_CASE__ __TEMPLATE_TABLENAME_LOWER__);

  @Delete("delete from __TEMPLATE_TABLENAME_LOWER__ where id=#{id}")
  void delete(@Param("id") long id);

}
