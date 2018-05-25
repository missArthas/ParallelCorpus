package com.missArthas.dao;

import com.missArthas.entity.UserEntity;

import java.util.List;

/**
 * Created by shhuang on 2016/12/13.
 */
public interface UserDao {
    public int insert(UserEntity user);
    public int delete(UserEntity user);
    public int update(UserEntity user);
    public UserEntity queryByPK(UserEntity user);
    public List<UserEntity> queryByUsername(String username);
    public List<UserEntity> queryLike(UserEntity user);
    public List<UserEntity> findAll();
}
