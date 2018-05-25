package com.missArthas.dao;

import com.missArthas.entity.AuthoritiesEntity;

import java.util.List;

/**
 * Created by shhuang on 2016/12/21.
 */
public interface AuthorityDao {
    public int insert(AuthoritiesEntity authoity);
    public int delete(AuthoritiesEntity authoity);
    public int update(AuthoritiesEntity authoity);
    public AuthoritiesEntity queryByPK(AuthoritiesEntity authoity);
    public List<AuthoritiesEntity> queryByUsername(String username);
    public List<AuthoritiesEntity> queryLike(AuthoritiesEntity authoity);
    public List<AuthoritiesEntity> findAll();
}
