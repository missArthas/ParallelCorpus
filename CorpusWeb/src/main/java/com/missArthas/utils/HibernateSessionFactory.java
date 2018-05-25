package com.missArthas.utils;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by shhuang on 2016/12/20.
 */
public class HibernateSessionFactory {
    private static Map<Thread, Session> sessionMap;
    private static SessionFactory sessionFactory;
    static {
        sessionMap = new HashMap<Thread, Session>();
        sessionFactory = new Configuration().configure().buildSessionFactory();
    }

    /**
     * can only use in web filter, beause it should remove and clear resources
     * @return
     */
    public static Session openSession() {
        System.out.println(Thread.currentThread().getStackTrace()[1] + " run in " + new Date());
        Session session = sessionMap.get(Thread.currentThread());
        if (session == null) {
            session = sessionFactory.openSession();
            sessionMap.put(Thread.currentThread(), session);
        }
        return session;
    }
    public static Session getCurrentSession() {
        return sessionMap.get(Thread.currentThread());
    }

    public static void closeAndRemoveSession() {
        System.out.println(Thread.currentThread().getStackTrace()[1]+ " run in " + new Date());//
        Session session = sessionMap.remove(Thread.currentThread());
        if (session != null) {
            session.close();
        }
    }
}
