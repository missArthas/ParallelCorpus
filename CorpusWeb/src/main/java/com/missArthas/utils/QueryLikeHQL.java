package com.missArthas.utils;

import com.missArthas.entity.UserEntity;

import java.lang.reflect.Field;

/**
 * Created by shhuang on 2016/12/21.
 */
public class QueryLikeHQL {
    public static String createQueryLikeHQL(Object o){
        String hql="from ";
        hql+=o.getClass().getSimpleName();
        hql+=" where ";
        Field[] fields = o.getClass().getDeclaredFields();
        for(Field field:fields){
            field.setAccessible(true);
            try {
                if(field.get(o)!=null&&!field.getName().equals("id")) {
                    hql=hql+field.getName()+" like :"+field.getName()+" and ";
                }
            } catch (IllegalAccessException e) {
                e.printStackTrace();
            }
        }
        hql+= "1=1";
        System.out.println(hql);
        return hql;
    }
    public static void main(String[] args) throws IllegalAccessException {
        UserEntity u = new UserEntity();
        //u.setId(0);
        u.setUsername("MarK");
        u.setPassword("123456");
        System.out.println(createQueryLikeHQL(u));
    }
}
