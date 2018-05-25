<div>
    <h2>Create a user account</h2>

    <form method="POST" action="user/reg">
            <table cellspacing="0">
                <tr>
                    <th><label>Username:</label></th>
                    <td><input id="username" name="username" type="text" size="15" maxlength="15" />
                        <small id="username_msg">No spaces, please.</small><br/>
                        <errors cssClass="error" />
                    </td>
                </tr>
                <tr>
                    <th><label>Password:</label></th>
                    <td><input id="password" name="password" type="password" size="15"
                                     showPassword="true"/>
                        <small>6 characters or more (be tricky!)</small><br/>
                        <errors cssClass="error" />
                    </td>
                </tr>
                <tr>
                    <th></th>
                    <td>
                    <button type="submit">I accept. Create my account.</button></td>
                </tr>
            </table>
    </form>
</div>

<script type="text/javascript" src="resources/js/jquery.min.js"></script>
<script>
    function submit(){
        var username=$("#username").val();
        var password=$("#password").val();
        $.ajax({
            type: "POST",
            url: "user/reg",
            data: {"username":username,
                "password":password},
            async: false,
            error: function (xhr, textStatus) {
                if (textStatus == 'timeout') {
                    alert("time out!");
                    response = null;
                } else {
                    alert("error，请刷新页面重试");
                }
            },
            success: function (data) {
            }
        });
    }
</script>
