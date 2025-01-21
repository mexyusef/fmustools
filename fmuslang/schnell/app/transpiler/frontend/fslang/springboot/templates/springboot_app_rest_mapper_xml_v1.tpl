<?xml version="1.0" encoding="UTF-8" ?>

<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="__TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__.__TEMPLATE_TABLENAME_CASE__Mapper">

  <select id="select__TEMPLATE_TABLENAME_CASE__ById" resultType="__TEMPLATE_TABLENAME_CASE__">
    select * from __TEMPLATE_TABLENAME_LOWER__ where id = #{id}
  </select>

  <select id="findAll" resultMap="__TEMPLATE_TABLENAME_LOWER__ResultMap">
    select * from __TEMPLATE_TABLENAME_LOWER__
  </select>

  <resultMap id="__TEMPLATE_TABLENAME_LOWER__ResultMap" type="__TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__TEMPLATE_TABLENAME_LOWER__.__TEMPLATE_TABLENAME_CASE__">
    <result property="id" column="id" />
    <result property="name" column="name" />
    <!-- <result property="state" column="state" />
    <result property="country" column="country" /> -->
  </resultMap>

  <insert id="insert">
    insert into __TEMPLATE_TABLENAME_LOWER__(
      name
      <!-- , state, country -->
    )
    values(
      #{__TEMPLATE_TABLENAME_LOWER__.name}
      <!-- ,
      #{__TEMPLATE_TABLENAME_LOWER__.state},
      #{__TEMPLATE_TABLENAME_LOWER__.country} -->
    )
  </insert>

  <update id="update__TEMPLATE_TABLENAME_CASE__">
    update __TEMPLATE_TABLENAME_LOWER__
      <set>
        <if test="__TEMPLATE_TABLENAME_LOWER__.name != null">name=#{__TEMPLATE_TABLENAME_LOWER__.name},</if>
        <!-- <if test="__TEMPLATE_TABLENAME_LOWER__.state != null">state=#{__TEMPLATE_TABLENAME_LOWER__.state},</if>
        <if test="__TEMPLATE_TABLENAME_LOWER__.country != null">country=#{__TEMPLATE_TABLENAME_LOWER__.country},</if> -->
      </set>
    where id=#{id}
  </update>


</mapper>
