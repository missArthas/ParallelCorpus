package com.missArthas.service;

import com.missArthas.entity.UserEntity;

import java.util.List;

/**
 * Created by shhuang on 2016/12/13.
 */
public interface UserService {
    public int insert(UserEntity user);
    public int insert(List<UserEntity> users);
    public int delete(UserEntity user);
    public int update(UserEntity user);
    public UserEntity queryByPK(UserEntity user);
    public List<UserEntity> queryLike(UserEntity user);
    public List<UserEntity> queryByUsername(String username);
    public List<UserEntity> findAll();
}
