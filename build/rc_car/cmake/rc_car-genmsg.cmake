# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "rc_car: 3 messages, 0 services")

set(MSG_I_FLAGS "-Irc_car:/home/andyklam/catkin_ws/src/rc_car/msg;-Isensor_msgs:/opt/ros/indigo/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(rc_car_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/drive_param.msg" NAME_WE)
add_custom_target(_rc_car_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rc_car" "/home/andyklam/catkin_ws/src/rc_car/msg/drive_param.msg" ""
)

get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/Lidar.msg" NAME_WE)
add_custom_target(_rc_car_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rc_car" "/home/andyklam/catkin_ws/src/rc_car/msg/Lidar.msg" ""
)

get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/pid_input.msg" NAME_WE)
add_custom_target(_rc_car_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rc_car" "/home/andyklam/catkin_ws/src/rc_car/msg/pid_input.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/drive_param.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rc_car
)
_generate_msg_cpp(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/Lidar.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rc_car
)
_generate_msg_cpp(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/pid_input.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rc_car
)

### Generating Services

### Generating Module File
_generate_module_cpp(rc_car
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rc_car
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(rc_car_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(rc_car_generate_messages rc_car_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/drive_param.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_cpp _rc_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/Lidar.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_cpp _rc_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/pid_input.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_cpp _rc_car_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rc_car_gencpp)
add_dependencies(rc_car_gencpp rc_car_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rc_car_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/drive_param.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rc_car
)
_generate_msg_lisp(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/Lidar.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rc_car
)
_generate_msg_lisp(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/pid_input.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rc_car
)

### Generating Services

### Generating Module File
_generate_module_lisp(rc_car
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rc_car
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(rc_car_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(rc_car_generate_messages rc_car_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/drive_param.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_lisp _rc_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/Lidar.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_lisp _rc_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/pid_input.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_lisp _rc_car_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rc_car_genlisp)
add_dependencies(rc_car_genlisp rc_car_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rc_car_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/drive_param.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rc_car
)
_generate_msg_py(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/Lidar.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rc_car
)
_generate_msg_py(rc_car
  "/home/andyklam/catkin_ws/src/rc_car/msg/pid_input.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rc_car
)

### Generating Services

### Generating Module File
_generate_module_py(rc_car
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rc_car
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(rc_car_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(rc_car_generate_messages rc_car_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/drive_param.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_py _rc_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/Lidar.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_py _rc_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andyklam/catkin_ws/src/rc_car/msg/pid_input.msg" NAME_WE)
add_dependencies(rc_car_generate_messages_py _rc_car_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rc_car_genpy)
add_dependencies(rc_car_genpy rc_car_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rc_car_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rc_car)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rc_car
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(rc_car_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rc_car)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rc_car
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(rc_car_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rc_car)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rc_car\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rc_car
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(rc_car_generate_messages_py sensor_msgs_generate_messages_py)
endif()
