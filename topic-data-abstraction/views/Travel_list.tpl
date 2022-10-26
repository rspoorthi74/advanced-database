<html>
<body>
<h2>Travel_list</h2>
<hr/>
<table>
% for item in Travel_list:
    <tr>

        <td>{{str(item['desc'])}}</td>
        <td><a href="/edit/{{str(item['id'])}}">edit</a></td>
        <td><a href="/delete/{{str(item['id'])}}">delete</a><td>
    </tr>
% end
</table>
<hr/>
<a href="/add">Addition of new Item...</a>
</body>
</html>
