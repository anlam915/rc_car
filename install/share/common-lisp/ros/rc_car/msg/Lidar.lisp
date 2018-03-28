; Auto-generated. Do not edit!


(cl:in-package rc_car-msg)


;//! \htmlinclude Lidar.msg.html

(cl:defclass <Lidar> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:integer
    :initform 0)
   (dist
    :reader dist
    :initarg :dist
    :type cl:float
    :initform 0.0))
)

(cl:defclass Lidar (<Lidar>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Lidar>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Lidar)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rc_car-msg:<Lidar> is deprecated: use rc_car-msg:Lidar instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <Lidar>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rc_car-msg:angle-val is deprecated.  Use rc_car-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'dist-val :lambda-list '(m))
(cl:defmethod dist-val ((m <Lidar>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rc_car-msg:dist-val is deprecated.  Use rc_car-msg:dist instead.")
  (dist m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Lidar>) ostream)
  "Serializes a message object of type '<Lidar>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'angle)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'angle)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'angle)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'angle)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dist))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Lidar>) istream)
  "Deserializes a message object of type '<Lidar>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'angle)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'angle)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'angle)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'angle)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dist) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Lidar>)))
  "Returns string type for a message object of type '<Lidar>"
  "rc_car/Lidar")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Lidar)))
  "Returns string type for a message object of type 'Lidar"
  "rc_car/Lidar")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Lidar>)))
  "Returns md5sum for a message object of type '<Lidar>"
  "6bbde98b68f84d3f9a872b55361580ba")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Lidar)))
  "Returns md5sum for a message object of type 'Lidar"
  "6bbde98b68f84d3f9a872b55361580ba")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Lidar>)))
  "Returns full string definition for message of type '<Lidar>"
  (cl:format cl:nil "uint32 angle~%float32 dist~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Lidar)))
  "Returns full string definition for message of type 'Lidar"
  (cl:format cl:nil "uint32 angle~%float32 dist~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Lidar>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Lidar>))
  "Converts a ROS message object to a list"
  (cl:list 'Lidar
    (cl:cons ':angle (angle msg))
    (cl:cons ':dist (dist msg))
))
