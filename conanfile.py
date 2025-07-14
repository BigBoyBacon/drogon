from conan import ConanFile
from conan.tools.cmake import cmake_layout


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        # self.requires("drogon/1.9.10")
        self.requires("jsoncpp/1.9.4")
        self.requires("zlib/1.2.11")
        # self.requires("gtest/1.10.0")
        self.requires("sqlite3/3.40.1")
        # self.requires("libpq/13.2")
        self.requires("libpq/15.12")
        self.requires("openssl/1.1.1t")
        # self.requires("hiredis/1.0.0")
        self.requires("brotli/1.0.9")

    # def layout(self):
    #     cmake_layout(self)