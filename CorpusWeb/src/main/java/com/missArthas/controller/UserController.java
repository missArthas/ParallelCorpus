package com.missArthas.controller;

import com.missArthas.entity.UserEntity;
import com.missArthas.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;

/**
 * Created by shhuang on 2016/12/14.
 */
@Controller
@RequestMapping("/main/user")
public class UserController {
    @Autowired
    private UserService userService;

    @RequestMapping(method = RequestMethod.GET,params = "new")
    public String index(Model model){
        model.addAttribute(new UserEntity());
        return "user/login";
    }

    @RequestMapping(value="/reg",method = RequestMethod.POST)
    public String registe(UserEntity user){
        userService.insert(user);
        return "redirect:"+user.getUsername();
    }

    @RequestMapping(value="/{username}",method = RequestMethod.GET)
    public String userdetail(@PathVariable String username, Model model){
        model.addAttribute("username",username);
        return "user/views";
    }

}
