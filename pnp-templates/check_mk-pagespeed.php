<?php
#
$opt[1] = "--vertical-label \"scores\" --title \"$hostname / $servicedesc\" ";

$def[1] = "DEF:var1=$RRDFILE[1]:$DS[1]:MAX ";
$def[1] .= "AREA:var1#2080ff:\"Performance\:\" ";
$def[1] .= "GPRINT:var1:LAST:\"%2.0lf scores\" ";
$def[1] .= "LINE1:var1#000080:\"\" ";
$def[1] .= "GPRINT:var1:MAX:\"(Max\: %2.0lf,\" ";
$def[1] .= "GPRINT:var1:MIN:\"Min\: %2.0lf,\" ";
$def[1] .= "GPRINT:var1:AVERAGE:\"Avg\: %2.0lf)\" ";

$opt[2] = "--vertical-label \"scores\" --title \"$hostname / $servicedesc\" ";

$def[2] = "DEF:var1=$RRDFILE[2]:$DS[2]:MAX ";
$def[2] .= "AREA:var1#66CD00:\"Performance\:\" ";
$def[2] .= "GPRINT:var1:LAST:\"%2.0lf scores\" ";
$def[2] .= "LINE1:var1#000080:\"\" ";
$def[2] .= "GPRINT:var1:MAX:\"(Max\: %2.0lf rpm,\" ";
$def[2] .= "GPRINT:var1:MIN:\"Min\: %2.0lf rpm,\" ";
$def[2] .= "GPRINT:var1:AVERAGE:\"Avg\: %2.0lf rpm)\" ";
?>