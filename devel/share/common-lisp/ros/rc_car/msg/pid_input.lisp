; Auto-generated. Do not edit!


(cl:in-package rc_car-msg)


;//! \htmlinclude pid_input.msg.html

(cl:defclass <pid_input> (roslisp-msg-protocol:ros-message)
  ((vel
    :reader vel
    :initarg :vel
    :type cl:float
    :initform 0.0)
   (error
    :reader error
    :initarg :error
    :type cl:float
    :initform 0.0))
)

(cl:defclass pid_input (<pid_input>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pid_input>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pid_input)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rc_car-msg:<pid_input> is deprecated: use rc_car-msg:pid_input instead.")))

(cl:ensure-generic-function 'vel-val :lambda-list '(m))
(cl:defmethod vel-val ((m <pid_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rc_car-msg:vel-val is deprecated.  Use rc_car-msg:vel instead.")
  (vel m))

(cl:ensure-generic-function 'error-val :lambda-list '(m))
(cl:defmethod error-val ((m <pid_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rc_car-msg:error-val is deprecated.  Use rc_car-msg:error instead.")
  (error m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pid_input>) ostream)
  "Serializes a message object of type '<pid_input>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vel))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'error))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pid_input>) istream)
  "Deserializes a message object of type '<pid_input>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vel) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'error) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pid_input>)))
  "Returns string type for a message object of type '<pid_input>"
  "rc_car/pid_input")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pid_input)))
  "Returns string type for a message object of type 'pid_input"
  "rc_car/pid_input")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pid_input>)))
  "Returns md5sum for a message object of type '<pid_input>"
  "fa47338c0346c1bbb44d6bdb6896f9d9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pid_input)))
  "Returns md5sum for a message object of type 'pid_input"
  "fa47338c0346c1bbb44d6bdb6896f9d9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pid_input>)))
  "Returns full string definition for message of type '<pid_input>"
  (cl:format cl:nil "float32 vel~%float32 error~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pid_input)))
  "Returns full string definition for message of type 'pid_input"
  (cl:format cl:nil "float32 vel~%float32 error~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pid_input>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pid_input>))
  "Converts a ROS message object to a list"
  (cl:list 'pid_input
    (cl:cons ':vel (vel msg))
    (cl:cons ':error (error msg))
))
