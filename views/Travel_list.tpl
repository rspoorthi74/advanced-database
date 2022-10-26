<html>
<body>
<table>
% for item in Travel_list:
    <tr>
        <td>{{str(item['id'])}}</td>
        <td>{{str(item['desc'])}}</td>
    </tr>
% end
</table>
</body>
</html>
