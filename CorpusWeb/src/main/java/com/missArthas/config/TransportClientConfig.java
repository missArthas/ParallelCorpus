package com.missArthas.config;

import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.net.InetAddress;
import java.net.UnknownHostException;

@Configuration
public class TransportClientConfig {
    @Bean(name="transportClient")
    public TransportClient init() throws UnknownHostException {
        Settings settings = Settings.settingsBuilder()
                .put("cluster.name", "parallel-corpus")
                .put("client.transport.sniff", true).build();

        TransportClient client = TransportClient.builder().settings(settings).build()
                .addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("192.168.1.101"), Integer.parseInt("9300")));
        return client;
    }
}
