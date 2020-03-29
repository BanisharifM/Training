import React from "react";
import {Link} from "react-router-dom";

const SideBar = () => {
    return (
        <ul>
            <li><Link to="/admin/posts">Posts</Link></li>
            <li><Link to="/admin/users">Users</Link></li>
        </ul>
    );
}
export default SideBar;