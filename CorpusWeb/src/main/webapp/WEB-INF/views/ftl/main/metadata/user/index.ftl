<h2 class="text-center heading">user列表</h2>
<div id="jsGrid"></div>
<script>

    $("#jsGrid").jsGrid({
        width: "100%",

        inserting: true,
        editing: true,
        sorting: true,
        paging: true,
        filtering: true,
        autoload: true,

        controller: {
            loadData: function (filter) {
                return $.ajax({
                    type: "GET",
                    url: "${request.contextPath}/metadata/user/detail.json",
                    data: filter
                });
            },

            insertItem: function (item) {
                return $.ajax({
                    type: "POST",
                    url: "${request.contextPath}/metadata/user/insert",
                    data: item
                });
            },

            updateItem: function (item) {
                return $.ajax({
                    type: "PUT",
                    url: "${request.contextPath}/metadata/user/update?id="+item.id+"&username="+item.username+"&password="+item.password,
                    data: item
                });
            },


            deleteItem: function (item) {
                return $.ajax({
                    type: "DELETE",
                    url: "${request.contextPath}/metadata/user/delete?id="+item.id,
                    data: item
                });
            },
        },

        pageSize: 15,
        pageButtonCount: 5,

        deleteConfirm: function (item) {
            return "The client \"" + item.username + "\" will be removed. Are you sure?";
        },
        rowClick: function (args) {
        },
        onItemInserting: function (args) {
            // cancel insertion of the item with empty 'name' field
            if (args.item.name === "") {
                args.cancel = true;
                alert("Specify the name of the item!");
            }
        },

        onItemInserted: function (args) {
            location.reload();
            //this.controller.loadData();
        },

        fields: [
            {name: "id", type: "number", width: 50, visible: false},
            {name: "username", type: "text", width: 50,align:"center"},
            {name: "password", type: "text", width: 200,align:"center"},
            {type: "control",align:"center"}
        ]
    });


</script>