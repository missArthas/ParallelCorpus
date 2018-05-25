package com.missArthas.service.impl;

import com.missArthas.dao.UserDao;
import com.missArthas.entity.UserEntity;
import com.missArthas.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Created by shhuang on 2016/12/13.
 */
@Service("userService")
public class UserServiceImpl implements UserService {

    @Autowired
    private UserDao userDao;

    public List<UserEntity> getAllUsernames() {
        return userDao.findAll();
    }

    public int insert(UserEntity user) {
        return userDao.insert(user);
    }

    public int insert(List<UserEntity> users) {
        int sum=0;
        for(UserEntity user:users){
            int result=userDao.insert(user);
            sum+=result;
        }
        return sum;
    }

    public int delete(UserEntity user) {
        return  userDao.delete(user);
    }

    public int update(UserEntity user) {
        return  userDao.update(user);
    }

    public UserEntity queryByPK(UserEntity user) {
        return userDao.queryByPK(user);
    }

    public List<UserEntity> queryLike(UserEntity user) {
        return userDao.queryLike(user);
    }

    public List<UserEntity> queryByUsername(String username) {
        return userDao.queryByUsername(username);
    }

    public List<UserEntity> findAll() {
        return userDao.findAll();
    }
}
