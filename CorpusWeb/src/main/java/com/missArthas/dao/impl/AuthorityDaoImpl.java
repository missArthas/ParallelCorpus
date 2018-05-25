package com.missArthas.dao.impl;

import com.missArthas.dao.AuthorityDao;
import com.missArthas.entity.AuthoritiesEntity;
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
public class AuthorityDaoImpl implements AuthorityDao {

    @Autowired
    private SessionFactory sessionFactory;

    public int insert(AuthoritiesEntity authoity) {
        int result = (Integer) sessionFactory.getCurrentSession().save(authoity);
        return result;
    }


    public int delete(AuthoritiesEntity authoityr) {
        sessionFactory.getCurrentSession().delete(authoityr);
        return 1;
    }

    public int update(AuthoritiesEntity authoity) {
        sessionFactory.getCurrentSession().saveOrUpdate(authoity);
        return 1;
    }

    public AuthoritiesEntity queryByPK(AuthoritiesEntity authoity) {
        AuthoritiesEntity result=(AuthoritiesEntity)sessionFactory.getCurrentSession().get(AuthoritiesEntity.class,authoity.getId());
        return result;
    }

    public List<AuthoritiesEntity> queryByUsername(String username) {
        String hql="from AuthoritiesEntity  where username=?";
        Query query=sessionFactory.getCurrentSession().createQuery(hql);
        query.setParameter(0,username);
        List<AuthoritiesEntity> authoritiesEntities=query.list();
        return authoritiesEntities;
    }

    public List<AuthoritiesEntity> queryLike(AuthoritiesEntity authoity) {
        String hql= QueryLikeHQL.createQueryLikeHQL(authoity);
        System.out.println(hql);
        Query query=sessionFactory.getCurrentSession().createQuery(hql);
        query.setProperties(authoity);
        List<AuthoritiesEntity> authoritiesEntities=query.list();
        return authoritiesEntities;
    }

    public List<AuthoritiesEntity> findAll() {
        Criteria criteria = sessionFactory.getCurrentSession().createCriteria(AuthoritiesEntity.class);
        return criteria.list();
    }
}
