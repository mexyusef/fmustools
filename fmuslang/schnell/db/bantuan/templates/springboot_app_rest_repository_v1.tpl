package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import org.springframework.data.jpa.repository.Query;

// https://stackoverflow.com/questions/33153271/how-do-you-create-a-spring-jpa-repository-findby-query-using-a-property-that-con
// Query
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
// import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;

@Repository
public interface __TEMPLATE_TABLENAME_CASE__Repository extends JpaRepository<__TEMPLATE_TABLENAME_CASE__, Long> {

  // @Select("select id, name from __TEMPLATE_TABLENAME_LOWER__ where id = #{id}")
  // __TEMPLATE_TABLENAME_CASE__ findById(@Param("id") Long id);

  // https://stackoverflow.com/questions/25362540/like-query-in-spring-jparepository
  // https://stackoverflow.com/questions/7491291/how-can-i-use-like-in-sql-queries-with-mybatis-safely-and-db-agnostic

  // @Query("select id, name from __TEMPLATE_TABLENAME_LOWER__ where name like %?1%")
  // @Query("select id, name from __TEMPLATE_TABLENAME_LOWER__ where name like %:name%")

  // Select gak bisa pake like spt Query
  // concat('%',concat(#{name}, '%'))
  // @Select("select id, name from __TEMPLATE_TABLENAME_LOWER__ where name like #{name}")
  // @Select("select id, name from __TEMPLATE_TABLENAME_LOWER__ where name like concat('%',concat(#{name}, '%'))")
  // @Select("select id, name from __TEMPLATE_TABLENAME_LOWER__ where name like '%' || #{name} || '%'")
  // List<__TEMPLATE_TABLENAME_CASE__> findByName(@Param("name") String name);

  List<__TEMPLATE_TABLENAME_CASE__> findByNameIgnoreCaseContaining(@Param("name") String name);

}
