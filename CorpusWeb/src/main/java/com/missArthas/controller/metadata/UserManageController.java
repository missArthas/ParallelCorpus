package com.missArthas.controller.metadata;

import com.missArthas.entity.UserEntity;
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
@RequestMapping("/main/metadata/user")
public class UserManageController {
    @Autowired
    UserService userService;


    @RequestMapping(method = RequestMethod.GET)
    public String index() {
        return "metadata/user/index";
    }

    @RequestMapping(value = "detail.json", method = RequestMethod.GET)
    public
    @ResponseBody
    List<UserEntity> getItems(String username) {
        UserEntity user = new UserEntity();
        if (username!=null&&username.length()!=0) {
            user.setUsername(username);
        }
        return userService.queryLike(user);
    }


    @RequestMapping(value = "insert", method = RequestMethod.POST)
    public
    @ResponseBody
    List<UserEntity> insert(UserEntity user) {
        userService.insert(user);
        return userService.queryLike(user);
    }

    @RequestMapping(value = "update", method = RequestMethod.PUT)
    public
    @ResponseBody
    UserEntity update(String id,String username,String password) {
        UserEntity user=new UserEntity();
        user.setId(Integer.parseInt(id));
        user.setUsername(username);
        user.setPassword(password);
        userService.update(user);
        return userService.queryByPK(user);
    }

    @RequestMapping(value = "delete", method = RequestMethod.DELETE)
    public String delete(String id) {
        UserEntity user=new UserEntity();
        user.setId(Integer.parseInt(id));
        if (user.getId() > 0) {
            userService.delete(user);
        }
        return index();

    }
}
