# Django_작성팁

---

- html에서 if로 hate에 포함되지 않는 항목,   
  그리고 길이가 2 이상인 항목은 3글자까지만 출력하도록 하는 법
  
  ```python
  {% for fruit in fruit_list %}
      {% if fruit in hate %}
      {% else %}
        {% if fruit|length >= 2 %}
          <p>{{fruit|truncatechars:3}}</p>
        {% endif %}
      {% endif %}
    {% endfor %}
  ```
  
  - Django에선 **|** 로 Built-in tag를 적용해준다.
