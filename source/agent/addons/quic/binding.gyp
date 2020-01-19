{
  'make_global_settings': [
    # ['CXX', '/home/jianjunz/code/quic/src/third_party/llvm-build/Release+Asserts/bin/clang++'],
    # ['CC', '/home/jianjunz/code/quic/src/third_party/llvm-build/Release+Asserts/bin/clang'],
    # ['LINK','/home/jianjunz/code/quic/src/third_party/llvm-build/Release+Asserts/bin/ld.lld'],
    # ['CXX', '/usr/bin/clang++'],
    # ['CC', '/usr/bin/clang'],
  ],
  'targets': [{
    'target_name': 'quic',
    'sources':[
      'addon.cc',
      'RTCIceTransport.cc',
      'RTCIceCandidate.cc',
      'RTCQuicTransport.cc',
      "QuicFactory.cc",
      #'RTCQuicTransportBase.cc',
      #'RTCCertificate.cc',
      #'P2PQuicTransport.cc',
      'IceConnectionAdapter.cc',
      #'QuicConnectionAdapter.cc',
      #'QuicStream.cc',
      #'../webrtc/webrtcLib/erizo/src/erizo/LibNiceConnection.cpp',
      '../../webrtc/webrtcLib/ThreadPool.cc',
      '../../webrtc/webrtcLib/IOThreadPool.cc',
      '../../../../third_party/licode/erizo/src/erizo/LibNiceConnection.cpp',
      '../../../../third_party/licode/erizo/src/erizo/IceConnection.cpp',
      '../../../../third_party/licode/erizo/src/erizo/lib/LibNiceInterfaceImpl.cpp',
      '../../../../third_party/licode/erizo/src/erizo/thread/IOThreadPool.cpp',
      '../../../../third_party/licode/erizo/src/erizo/thread/IOWorker.cpp',
      '../../../../third_party/licode/erizo/src/erizo/thread/Scheduler.cpp',
      '../../../../third_party/licode/erizo/src/erizo/thread/ThreadPool.cpp',
      '../../../../third_party/licode/erizo/src/erizo/thread/Worker.cpp',
      '../../../core/owt_base/MediaFramePipeline.cpp',
      '../../../core/owt_base/MediaFrameMulticaster.cpp',
    ],
    'defines':[
      'OWT_ENABLE_QUIC=1',
    ],
    'cflags':[
      # '-nostdinc++',
      # '-isystem/home/jianjunz/code/quic/src/buildtools/third_party/libc++/trunk/include',
      # '-isystem/home/jianjunz/code/quic/src/buildtools/third_party/libc++abi/trunk/include',
    ],
    'cflags_cc': [
      '-std=gnu++14',
      '-fno-exceptions',
      '-DWEBRTC_POSIX',
      '-DWEBRTC_LINUX',
      '-DLINUX',
      '-DNOLINUXIF',
      '-DNO_REG_RPC=1',
      '-DHAVE_VFPRINTF=1',
      '-DRETSIGTYPE=void',
      '-DNEW_STDIO',
      '-DHAVE_STRDUP=1',
      '-DHAVE_STRLCPY=1',
      '-DHAVE_LIBM=1',
      '-DHAVE_SYS_TIME_H=1',
      '-DTIME_WITH_SYS_TIME_H=1',
      # '-nostdinc++',
      '-Wno-non-pod-varargs',
      '-fPIC',
      # '-I/usr/lib/llvm-9/include/c++/v1',
      # '-isystem/home/jianjunz/code/quic/src/buildtools/third_party/libc++/trunk/include',
      # '-isystem/home/jianjunz/code/quic/src/buildtools/third_party/libc++abi/trunk/include',
    ],
    'include_dirs': [
      "<!(node -e \"require('nan')\")",
      'conn_handler',
      '../webrtc/webrtcLib/erizo/src/erizo',
      '../../../../third_party/licode/erizo/src/erizo',
      '../../../../third_party/licode/erizo/src/erizo/lib',
      '../../../../third_party/licode/erizo/src/erizo/thread',
      '../../../../third_party/licode/erizo/src/erizo/stats',
      '../../../core/common',
      '../../../core/owt_base',
      '../../../../build/libdeps/build/include',
      '/home/jianjunz/code/quic/src/owt/quic_transport/api',
      '<!@(pkg-config glib-2.0 --cflags-only-I | sed s/-I//g)',
    ],
    'ldflags': [
      '-Wl,--no-as-needed',
      '-Wl,-rpath,/home/jianjunz/code/quic/src/out/debug',
      '-L$(CORE_HOME)/../../build/libdeps/build/lib',
      '-fPIC',
      #'-L/home/jianjunz/code/quic/src/out/debug/obj/owt/quic_transport',
      '-L/home/jianjunz/code/quic/src/out/debug',
    ],
    'cflags_cc!': [
      '-std=gnu++0x',
      '-fno-exceptions',
    ],
    'libraries': [
      '-ldl',
      '-llog4cxx',
      '-lboost_thread',
      '-lboost_system',
      '-lnice',
      '-lowt_quic_transport',
      # '-lc++',
      # '-lc++abi',
      # '-lm',
      # '-lc',
      # '-lgcc_s',
      # '-lgcc',
    ],
  }]
}