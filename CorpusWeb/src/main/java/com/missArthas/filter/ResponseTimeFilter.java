package com.missArthas.filter;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

public class ResponseTimeFilter implements Filter {

    public void init(FilterConfig filterConfig) throws ServletException {

    }

    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        HttpServletRequest req = (HttpServletRequest)servletRequest;

        long t1 = System.currentTimeMillis();

        filterChain.doFilter(servletRequest, servletResponse);

        long t2 = System.currentTimeMillis();

        System.out.println("***servletRequest (" + req.getRequestURI() + ") finished with time(ms):" + (t2-t1) );
    }

    public void destroy() {

    }
}
