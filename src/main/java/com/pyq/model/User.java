package com.pyq.model;

import jakarta.persistence.*;

@Entity
public class User {

 @Id
 @GeneratedValue(strategy = GenerationType.IDENTITY)
 private int id;

 private String name;
 private String enrollment;
 private String email;      // ✅ ADD
 private String password;
 private String role;       // ✅ ADD (ADMIN / USER)

 // getters setters

 public int getId(){ return id; }

 public String getName(){ return name; }
 public void setName(String n){ this.name = n; }

 public String getEnrollment(){ return enrollment; }
 public void setEnrollment(String e){ this.enrollment = e; }

 public String getEmail(){ return email; }
 public void setEmail(String e){ this.email = e; }

 public String getPassword(){ return password; }
 public void setPassword(String p){ this.password = p; }

 public String getRole(){ return role; }
 public void setRole(String r){ this.role = r; }
}