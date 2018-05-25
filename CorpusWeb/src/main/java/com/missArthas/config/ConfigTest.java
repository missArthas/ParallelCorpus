package com.missArthas.config;

import org.springframework.beans.factory.InitializingBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.FilterType;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@Configuration
public class ConfigTest {
    @Bean(name="testBean")
    public InitializingBean init(){
        return new InitializingBean(){
            @Override
            public void afterPropertiesSet() throws Exception {
                System.out.println("这个没初始化");
            }
        };
    }
}
