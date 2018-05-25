<html>
<head>
    <link rel="stylesheet" type="text/css" media="screen"
          href="/resources/css/bootstrap.min.css">

    <script type="text/javascript" src="/resources/js/jquery.min.js'"></script>
    <script type="text/javascript" src="/resources/js/jqueryui/jquery-ui.min.js"></script>
    <script type="text/javascript" src="/resources/js/jqueryui/jquery-ui.js"></script>
</head>

<body>
<div align="center">
</div>
<div align="center" style="height: 200px">
    <img src="/resources/img/seu_logo.jpeg" height="100" width="311">
    <form action="search" method="post" accept-charset="UTF-8" class="bs-example bs-example-form" style="width: 324px;">
        <div class="input-group">
            <input class="form-control" type="text" name="keyword" value="${keyword?if_exists}"/>
            <span class="input-group-btn">
                        <button class="btn btn-default" type="submit">搜索</button>
            </span>
        </div>
        <div>
            <input type="radio" name="language" value='chinese' <#if language?? && language = 'chinese'>checked</#if>/>
            <label>中文->English</label>
            <input type="radio" name="language" value="english" <#if language?? && language = 'english'>checked</#if>/>
            <label>English->中文</label>
        </div>
    </form>
</div>
<div class="panel panel-primary" style="margin-top:5px;margin-bottom:5px">
    <div class="panel-heading" style="height:40px">
        <#if keyword ??><p style="float:left">搜索：${keyword}</p></#if>
        <#if totalRecords ??><p style="float:right">共${totalRecords}条</p></#if>
    </div>
    <div style="clear:both"></div>
    <div class="panel-body" style="height:40px;padding:10px 15px">
        详细信息：
    </div>
</div>
<ul class="pager" style="float:right; margin:0px 15px 0px 0px">
    <button type="submit" class="btn btn-pager" name="first">首页</button>
    <button type="submit" class="btn btn-pager" name="previous">上页</button>
    <button type="submit" class="btn btn-pager" name="next">下页</button>
    <button type="submit" class="btn btn-pager" name="last">末页</button>
</ul>
    <#if language ??>
        <table class="table table-striped">
        <#if language = 'chinese'>
            <#if hits??>
                <#list hits as hit>
                    <tr><td>${hit_index+1}</td><td>${hit.chinese}</td></tr>
                    <tr><td></td><td>${hit.english}</td></tr>
                    <tr><td></td><td>语料来源：${hit.web_source}</td></tr>
                </#list>
            </#if>
        <#else>
            <#if hits??>
                <#list hits as hit>
                    <tr><td>${hit_index+1}</td><td>${hit.english}</td></tr>
                    <tr><td></td><td>${hit.chinese}</td></tr>
                    <tr><td></td><td>语料来源：${hit.web_source}</td></tr>
                </#list>
            </#if>
        </#if>
        </table>
    </#if>

<ul class="pager" style="float:right; margin:0px 15px 0px 0px">
    <button type="submit" class="btn btn-pager" name="first">首页</button>
    <button type="submit" class="btn btn-pager  disabled " name="previous">上页</button>
    <button type="submit" class="btn btn-pager  disabled " name="next">下页</button>
    <button type="submit" class="btn btn-pager" name="last">末页</button>
</ul>
</body>
</html>