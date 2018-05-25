package com.missArthas.service;

import com.missArthas.entity.AuthoritiesEntity;
import com.missArthas.entity.UserEntity;

import java.util.List;

/**
 * Created by shhuang on 2016/12/13.
 */
public interface AuthorityService {
    public int insert(AuthoritiesEntity authoity);
    public int delete(AuthoritiesEntity authoity);
    public int update(AuthoritiesEntity authoity);
    public AuthoritiesEntity queryByPK(AuthoritiesEntity authoity);
    public List<AuthoritiesEntity> queryByUsername(String username);
    public List<AuthoritiesEntity> queryLike(AuthoritiesEntity authoity);
    public List<AuthoritiesEntity> findAll();
}
