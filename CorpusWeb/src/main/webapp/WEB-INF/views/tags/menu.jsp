<%@ taglib prefix="sec"
	uri="http://www.springframework.org/security/tags"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags" prefix="s" %>
<%@ page language="java" contentType="text/html; charset=utf-8"
	pageEncoding="utf-8"%>

<script type="text/javascript">
	$(document).ready(function () {
		$('.inactives').click(function () {
			if ($(this).siblings('ul').css('display') == 'none') {
				$(this).parent('li').siblings('li').removeClass('inactives');
				$(this).addClass('inactives');
				$(this).siblings('ul').slideDown(100).children('li');
				if ($(this).parents('li').siblings('li').children('ul').css('display') == 'block') {
					$(this).parents('li').siblings('li').children('ul').parent('li').children('a').removeClass('inactives');
					$(this).parents('li').siblings('li').children('ul').slideUp(100);
				}
			} else {
				//控制自身变成+号
				$(this).removeClass('inactives');
				//控制自身菜单下子菜单隐藏
				$(this).siblings('ul').slideUp(100);
				//控制自身子菜单变成+号
				$(this).siblings('ul').children('li').children('ul').parent('li').children('a').addClass('inactives');
				//控制自身菜单下子菜单隐藏
				$(this).siblings('ul').children('li').children('ul').slideUp(100);

				//控制同级菜单只保持一个是展开的（-号显示）
				$(this).siblings('ul').children('li').children('a').removeClass('inactives');
			}
		})
	});
</script>
<!-- User info -->
<div class="login-info">

		<a href="javascript:void(0);" id="show-shortcut"
		data-action="toggleShortcut"> 
		<img src="<c:url value='/resources/img/sunny.png' />" alt="me" class="online" /> <span>:
				<sec:authentication property="principal.username" />
		</span>
	</a>
</div>

<div class="list">
	<ul class="yiji">
		<li><a href="#" class="inactives">一级目录</a>
			<ul style="display: block">
				<li><a href="#" class="inactives active">二级目录</a>
					<ul style="display: none">
						<li><a href=<c:url value='#'/>>三级目录</a></li>
						<li><a href=<c:url value='#'/>>三级目录</a></li>
						<li><a href=<c:url value='#'/>>三级目录</a></li>
					</ul>
				</li>
				<li><a href="#" class="inactives active">二级目录</a>
					<ul style="display: none">
						<li><a href=<c:url value='#'/>>三级目录</a></li>
						<li><a href=<c:url value='#'/>>三级目录</a></li>
					</ul>
				</li>
			</ul>
		</li>
		<li><a href="#" class="inactives">一级目录</a>
			<ul style="display: block">
				<li class="last"><a href="#">二级目录</a></li>
				<li><a href="#" class="inactives active">维表管理</a>
					<ul style="display: none">
						<li><a href="<c:url value="/metadata/user"/>">user表</a></li>
						<li><a href="<c:url value="/metadata/authority"/>">authorities表</a></li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
</div>

<span class="minifyme" data-action="minifyMenu">
	<i class="fa fa-arrow-circle-left hit"></i>
</span>



