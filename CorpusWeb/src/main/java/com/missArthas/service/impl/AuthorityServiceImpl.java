package com.missArthas.service.impl;

import com.missArthas.dao.AuthorityDao;
import com.missArthas.entity.AuthoritiesEntity;
import com.missArthas.service.AuthorityService;
import com.missArthas.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Created by shhuang on 2016/12/13.
 */
@Service("authorityService")
public class AuthorityServiceImpl implements AuthorityService {

    @Autowired
    private AuthorityDao authorityDao;

    public List<AuthoritiesEntity> getAllUsernames() {
        return authorityDao.findAll();
    }

    public int insert(AuthoritiesEntity authority) {
        return authorityDao.insert(authority);
    }

    public int insert(List<AuthoritiesEntity> authorities) {
        int sum=0;
        for(AuthoritiesEntity authoity:authorities){
            int result=authorityDao.insert(authoity);
            sum+=result;
        }
        return sum;
    }

    public int delete(AuthoritiesEntity authority) {
        return  authorityDao.delete(authority);
    }

    public int update(AuthoritiesEntity authoity) {
        return authorityDao.update(authoity);
    }

    public AuthoritiesEntity queryByPK(AuthoritiesEntity authoity) {
        return authorityDao.queryByPK(authoity);
    }

    public List<AuthoritiesEntity> queryByUsername(String username) {
        return authorityDao.queryByUsername(username);
    }

    public List<AuthoritiesEntity> queryLike(AuthoritiesEntity authoity) {
        return authorityDao.queryLike(authoity);
    }

    public List<AuthoritiesEntity> findAll() {
        return authorityDao.findAll();
    }
}
