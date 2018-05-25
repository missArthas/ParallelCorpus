package com.missArthas.controller;

import com.missArthas.config.ConfigTest;
import com.missArthas.config.TransportClientConfig;
import com.missArthas.entity.UserEntity;
import com.missArthas.service.AuthorityService;
import com.missArthas.service.UserService;
import org.elasticsearch.search.SearchHit;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.action.search.SearchType;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;
import org.elasticsearch.search.SearchHits;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import java.io.UnsupportedEncodingException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.net.UnknownServiceException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import com.alibaba.fastjson.JSON;

/**
 * Created by shhuang on 2016/12/28.
 */
@Controller
@RequestMapping("/")
public class MainController {
    @Autowired
    private UserService userService;

    @Autowired
    private AuthorityService authorityService;

    @Autowired
    private TransportClient transportClient;

    @RequestMapping()
    public String index(){
        return "corpus/index";
    }

    @RequestMapping(value = "/loginPage",method = RequestMethod.GET)
    public String loginPage(@RequestParam(value = "error", required = false) String error) {
        if (error != null) {
            return "security/login";
        }
        return "security/login";
    }

    @RequestMapping(value = "/main",method = RequestMethod.GET)
    public String main() {
        return "main/hello/index";
    }

    @RequestMapping(value = "/registePage",method = RequestMethod.GET)
    public String registePage(){
        return "security/reg";
    }

    @RequestMapping(value = "/registe",method = RequestMethod.GET)
    public String registe(){
        return "security/login";
    }

    @RequestMapping(value = "/project",method = RequestMethod.GET)
    public String manageProject(){
        return "project/index";
    }

    @RequestMapping(value = "/translate",method = RequestMethod.GET)
    public String translate(){
        return "translate/index";
    }

    @RequestMapping(value = "/corpus",method = RequestMethod.GET)
    public String corpus() throws UnknownHostException {
//        Settings settings = Settings.settingsBuilder()
//                .put("cluster.name", "parallel-corpus")
//                .put("client.transport.sniff", true).build();
//
//        TransportClient client = TransportClient.builder().settings(settings).build()
//                .addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("localhost"), Integer.parseInt("9300")));

        SearchResponse response = transportClient.prepareSearch("corpus")
                .setTypes("pair")
                .setQuery(QueryBuilders.termQuery("chinese", "他们"))
                .execute()
                .actionGet();
        SearchHits searchHits = response.getHits();
        System.out.println("-----------------在["+"chinese"+"]中搜索关键字["+"他们"+"]---------------------");
        System.out.println("共匹配到:"+searchHits.getTotalHits()+"条记录!");
        return "corpus/index";
    }

    @RequestMapping(value = "/search",method = RequestMethod.POST)
    @ResponseBody
    public ModelAndView search(HttpServletRequest request){
        ModelAndView mv = new ModelAndView();

        try {
            request.setCharacterEncoding("UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }

        String keyword=request.getParameter("keyword");
        String language=request.getParameter("language");
        SearchResponse response = transportClient.prepareSearch("corpus")
                .setTypes("pair")
                .setQuery(QueryBuilders.termQuery(language, keyword))
                .setSize(50)
                .setFrom(10)
                .execute()
                .actionGet();

        SearchHits searchHits = response.getHits();
        List list = new ArrayList<Map<String, Object>>();

        for(SearchHit hit:searchHits){
            Map<String, Object> t = hit.getSource();
            list.add(t);
            System.out.println(t);
        }


        mv.addObject("totalRecords", searchHits.getTotalHits());
        mv.addObject("keyword", keyword);
        mv.addObject("hits", list);
        mv.addObject("language", language);
        mv.setViewName("corpus/index");
        return mv;
    }

    @RequestMapping(value = "/searchtest",method = RequestMethod.GET,produces="application/json")
    @ResponseBody
    public String searchtest(String keyword, String language, int size, int from){


        SearchResponse response = transportClient.prepareSearch("corpus")
                .setTypes("pair")
                .setQuery(QueryBuilders.termQuery(language, keyword))
                .setSize(size)
                .setFrom(from)
                .execute()
                .actionGet();

        SearchHits searchHits = response.getHits();
        List list = new ArrayList<Map<String, Object>>();

        for(SearchHit hit:searchHits){
            Map<String, Object> t = hit.getSource();
            list.add(t);
        }


        return JSON.toJSONString(list);
    }


}
