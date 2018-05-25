package com.missArthas.dao.impl;

import com.missArthas.dao.UserDao;
import com.missArthas.entity.UserEntity;
import com.missArthas.utils.QueryLikeHQL;
import org.hibernate.Criteria;
import org.hibernate.Query;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 * Created by shhuang on 2016/12/13.
 */
@Repository
@Transactional
public class UserDaoImpl implements UserDao {

    @Autowired
    private SessionFactory sessionFactory;

    public int insert(UserEntity u) {
        int result = (Integer) sessionFactory.getCurrentSession().save(u);
        return result;
    }


    public int delete(UserEntity user) {
        sessionFactory.getCurrentSession().delete(user);
        return 1;
    }

    public int update(UserEntity user) {
        sessionFactory.getCurrentSession().saveOrUpdate(user);
        return 1;
    }

    public UserEntity queryByPK(UserEntity user) {
        UserEntity result=(UserEntity)sessionFactory.getCurrentSession().get(UserEntity.class,user.getId());
        return result;
    }

    public List<UserEntity> queryByUsername(String username) {
        String hql="from UserEntity  where username=?";
        Query query=sessionFactory.getCurrentSession().createQuery(hql);
        query.setParameter(0,username);
        List<UserEntity> userEntities=query.list();
        return userEntities;
    }

    public List<UserEntity> queryLike(UserEntity user) {
        //String hql="from UserEntity where username like :username and password like :password and 1=1";
        String hql= QueryLikeHQL.createQueryLikeHQL(user);
        System.out.println(hql);
        Query query=sessionFactory.getCurrentSession().createQuery(hql);
        query.setProperties(user);
        //query.setParameter(0,user.getUsername());
        List<UserEntity> userEntities=query.list();
        return userEntities;
    }


    public List<UserEntity> findAll() {
        Criteria criteria = sessionFactory.getCurrentSession().createCriteria(UserEntity.class);
        return criteria.list();
    }
}
