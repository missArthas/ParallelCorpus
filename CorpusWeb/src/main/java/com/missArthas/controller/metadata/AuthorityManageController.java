package com.missArthas.controller.metadata;

import com.missArthas.entity.AuthoritiesEntity;
import com.missArthas.entity.UserEntity;
import com.missArthas.service.AuthorityService;
import com.missArthas.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

/**
 * Created by shhuang on 2016/12/12.
 */
@Controller
@RequestMapping("/main/metadata/authority")
public class AuthorityManageController {
    @Autowired
    AuthorityService authorityService;

    @RequestMapping(method = RequestMethod.GET)
    public String index() {
        return "metadata/authority/index";
    }

    @RequestMapping(value = "detail.json", method = RequestMethod.GET)
    public
    @ResponseBody
    List<AuthoritiesEntity> getItems(String username) {
        AuthoritiesEntity authority = new AuthoritiesEntity();
        if (username!=null&&username.length()!=0) {
            authority.setUsername(username);
        }
        return authorityService.queryLike(authority);
    }

    @RequestMapping(value = "insert", method = RequestMethod.POST)
    public
    @ResponseBody
    List<AuthoritiesEntity> insert(AuthoritiesEntity authority) {
        authorityService.insert(authority);
        return authorityService.queryLike(authority);
    }

    @RequestMapping(value = "update", method = RequestMethod.PUT)
    public
    @ResponseBody
    AuthoritiesEntity update(String id,String username,String authority) {
        AuthoritiesEntity authoritiesEntity=new AuthoritiesEntity();
        authoritiesEntity.setId(Integer.parseInt(id));
        authoritiesEntity.setUsername(username);
        authoritiesEntity.setAuthority(authority);
        authorityService.update(authoritiesEntity);
        return authorityService.queryByPK(authoritiesEntity);
    }

    @RequestMapping(value = "delete", method = RequestMethod.DELETE)
    public String delete(String id) {
        AuthoritiesEntity authoritiesEntity=new AuthoritiesEntity();
        authoritiesEntity.setId(Integer.parseInt(id));
        if (authoritiesEntity.getId() > 0) {
            authorityService.delete(authoritiesEntity);
        }
        return index();
    }
}
