import React from "react";

const Like = ({ isLiked, onToggle }) => {
  let classNm = "fa fa-heart";
  if (!isLiked) classNm += "-o";
  //   console.log(this.props);
  return (
    <i onClick={onToggle} style={{ cursor: "pointer" }} className={classNm}></i>
  );
};

export default Like;
