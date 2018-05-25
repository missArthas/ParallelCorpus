package com.missArthas.test;

import com.missArthas.entity.UserEntity;

import java.lang.reflect.Field;

/**
 * Created by shhuang on 2016/12/20.
 */
public class Test {
    public static void main(String[] args) throws Exception{
        UserEntity u = new UserEntity();
        u.setId(0);
        u.setUsername("MarK");
        u.setPassword("123456");
        Field[] fields = u.getClass().getDeclaredFields();
        for(int i=0; i<fields.length; i++){
            Field f = fields[i];
            f.setAccessible(true);
            System.out.println("属性名:" + f.getName() + " 属性值:" + f.get(u));
        }

    }
}
